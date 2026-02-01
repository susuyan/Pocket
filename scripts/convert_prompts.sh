#!/bin/bash

# 转换 prompts 目录中的 markdown 文件为 JSON
# 输出到 raycast-extensions/prompt-extension/data/prompts.json

PROMPTS_DIR="/Users/susuyan/Workspace/Pocket/prompts"
OUTPUT_FILE="/Users/susuyan/Workspace/Pocket/raycast-extensions/prompt-extension/data/prompts.json"

# 确保输出目录存在
mkdir -p "$(dirname "$OUTPUT_FILE")"

# 初始化 JSON 数组
json_array="["
first=true

# 遍历所有 .md 文件（排除 README.md）
for file in "$PROMPTS_DIR"/*.md; do
    # 跳过 README.md
    if [[ "$(basename "$file")" == "README.md" ]]; then
        continue
    fi
    
    # 读取文件内容
    content=$(cat "$file")
    
    # 提取 YAML frontmatter
    name=$(echo "$content" | sed -n '/^---$/,/^---$/p' | grep "^name:" | sed 's/^name: *//' | sed 's/^"//;s/"$//')
    description=$(echo "$content" | sed -n '/^---$/,/^---$/p' | grep "^description:" | sed 's/^description: *//' | sed 's/^"//;s/"$//')
    
    # 提取提示词内容（第二个 --- 之后的内容）
    prompt=$(echo "$content" | awk '/^---$/{count++} count==2{getline; print; exit}')
    
    # 如果第一行是空行，读取下一行
    if [[ -z "$prompt" ]]; then
        prompt=$(echo "$content" | awk '/^---$/{count++} count==2{getline; if(NF>0) print; else {getline; print}}')
    fi
    
    # 转义特殊字符
    name=$(echo "$name" | sed 's/"/\\"/g')
    description=$(echo "$description" | sed 's/"/\\"/g')
    prompt=$(echo "$prompt" | sed 's/"/\\"/g')
    
    # 添加到 JSON 数组
    if [ "$first" = true ]; then
        first=false
    else
        json_array="$json_array,"
    fi
    
    json_array="$json_array{\"name\":\"$name\",\"description\":\"$description\",\"prompt\":\"$prompt\"}"
done

json_array="$json_array]"

# 输出压缩后的 JSON
echo "$json_array" > "$OUTPUT_FILE"

echo "已生成: $OUTPUT_FILE"
