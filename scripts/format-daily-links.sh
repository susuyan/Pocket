#!/usr/bin/env bash
set -euo pipefail
TARGET="${1:-docs/daily-links/$(date +%F).md}"
if [ ! -f "$TARGET" ]; then
  exit 0
fi
TMP="$(mktemp)"
awk '
BEGIN{
  header=""
  in_section=0
}
NR==1 && $0 ~ /^# Daily Links /{
  header=$0
  next
}
$0 ~ /^## /{
  if (in_section==1) {
    keep=0
    for (i=1;i<=n;i++){
      line=section[i]
      gsub(/[[:space:]]+$/,"",line)
      if (line !~ /^[[:space:]]*$/ && line !~ /^---$/) {
        keep=1
        break
      }
    }
    if (keep==1) {
      kept_sections_count++
      kept_header[kept_sections_count]=current_header
      kept_n[kept_sections_count]=n
      for (i=1;i<=n;i++){ kept_section[kept_sections_count,i]=section[i] }
    }
    delete section
    n=0
  }
  current_header=$0
  in_section=1
  next
}
{
  if (in_section==1) {
    section[++n]=$0
  } else {
    preface[++pref_n]=$0
  }
}
END{
  # finalize last section
  if (in_section==1) {
    keep=0
    for (i=1;i<=n;i++){
      line=section[i]
      gsub(/[[:space:]]+$/,"",line)
      if (line !~ /^[[:space:]]*$/ && line !~ /^---$/) {
        keep=1
        break
      }
    }
    if (keep==1) {
      kept_sections_count++
      kept_header[kept_sections_count]=current_header
      kept_n[kept_sections_count]=n
      for (i=1;i<=n;i++){ kept_section[kept_sections_count,i]=section[i] }
    }
  }
  # print header
  print header
  # print any preface lines (unlikely)
  for (i=1;i<=pref_n;i++){ print preface[i] }
  # print sections with separators and normalized blank lines
  for (s=1;s<=kept_sections_count;s++){
    print ""
    print kept_header[s]
    print ""
    prevblank=0
    for (i=1;i<=kept_n[s];i++){
      line=kept_section[s,i]
      gsub(/[[:space:]]+$/,"",line)
      if (line ~ /^---$/) {
        continue
      } else if (line ~ /^[[:space:]]*$/) {
        if (prevblank==0){ print ""; prevblank=1 }
      } else {
        print line
        prevblank=0
      }
    }
    if (s<kept_sections_count){
      print ""
      print "---"
    }
  }
}
' "$TARGET" > "$TMP"
mv "$TMP" "$TARGET"
