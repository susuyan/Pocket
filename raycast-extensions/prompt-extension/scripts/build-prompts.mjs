#!/usr/bin/env node
import fs from "fs";
import path from "path";
import matter from "gray-matter";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROMPTS_DIR = path.join(__dirname, "..", "prompts");
const OUTPUT_FILE = path.join(__dirname, "..", "data", "prompts.json");

function buildPrompts() {
  // 确保 data 目录存在
  const dataDir = path.dirname(OUTPUT_FILE);
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }

  // 检查 prompts 目录是否存在
  if (!fs.existsSync(PROMPTS_DIR)) {
    console.log("⚠️ prompts/ directory not found, creating...");
    fs.mkdirSync(PROMPTS_DIR, { recursive: true });
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify([], null, 2));
    console.log("✓ Created empty prompts.json");
    return;
  }

  // 读取所有 md 文件
  const files = fs
    .readdirSync(PROMPTS_DIR)
    .filter((f) => f.endsWith(".md"))
    .sort();

  if (files.length === 0) {
    console.log("⚠️ No .md files found in prompts/");
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify([], null, 2));
    return;
  }

  const prompts = [];

  for (const file of files) {
    const filePath = path.join(PROMPTS_DIR, file);
    const raw = fs.readFileSync(filePath, "utf8");
    const parsed = matter(raw);

    const { name, description } = parsed.data;
    const content = parsed.content.trim();

    if (!name || !content) {
      console.warn(`⚠️ Skipping ${file}: missing 'name' or content`);
      continue;
    }

    prompts.push({
      name,
      description: description || "",
      content,
    });

    console.log(`  ✓ ${file} → ${name}`);
  }

  // 写入 JSON
  fs.writeFileSync(OUTPUT_FILE, JSON.stringify(prompts, null, 2));
  console.log(`\n✓ Generated ${OUTPUT_FILE} (${prompts.length} prompts)`);
}

buildPrompts();
