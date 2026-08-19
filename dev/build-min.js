// 保守压缩：保留 /*! 头注释，移除其余注释与缩进，保持行为与源码一致
const fs = require('fs');
const path = require('path');

const src = path.join(__dirname, '..', 'dev', 'js', 'index.js');
const out = path.join(__dirname, '..', 'assets', 'js', 'index.min.js');

let code = fs.readFileSync(src, 'utf8');

// 提取头部 bang 注释（如有）
let header = '';
const bang = /^(\/\*![\s\S]*?\*\/)/.exec(code);
if (bang) {
  header = bang[1].replace(/\s*\n\s*/g, '\n') + '\n';
  code = code.slice(bang[0].length);
}

// 移除注释（字符串中无 '//' 与 '/*' 字面量，安全）
code = code
  .replace(/\/\*[\s\S]*?\*\//g, '')   // 块注释
  .replace(/(^|[^:])\/\/.*$/gm, '$1') // 行注释
  .split('\n')
  .map((l) => l.trim())
  .filter((l) => l.length > 0)
  .join('\n');

fs.writeFileSync(out, header + code + '\n', 'utf8');
console.log('written:', out, (header + code).length, 'bytes');
