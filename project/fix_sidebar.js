const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

// 1. Remove specific icons (bullseye, book, plug, envelope-open-text)
content = content.replace(/<i class="fa-solid fa-bullseye[^>]+><\/i>/g, '');
content = content.replace(/<i class="fa-solid fa-book[^>]+><\/i>/g, '');
content = content.replace(/<i class="fa-solid fa-plug[^>]+><\/i>/g, '');
content = content.replace(/<i class="fa-solid fa-envelope-open-text[^>]+><\/i>/g, '');
// Also remove any extra whitespace left behind (e.g. newline and spaces before the span)
content = content.replace(/<\/a>/g, '</a>'); // just to ensure no issues

// 2. Remove inconsistent small font sizes
content = content.replace(/text-\[11px\]/g, 'text-sm');
content = content.replace(/text-\[12px\]/g, 'text-sm');
content = content.replace(/text-\[13px\]/g, 'text-sm');

// 3. To make it consistent, the root items in the sidebar have ont-bold. 
// The user said "子目录字体一致" meaning all subdirectories should have the same font size.
// By replacing the 11px/12px with text-sm, they will now be text-sm (14px).

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
