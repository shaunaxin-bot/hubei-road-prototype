const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

// Increase font sizes
content = content.replace(/text-xs/g, 'text-sm');
content = content.replace(/text-sm/g, 'text-base');

// Minimize line spacing
content = content.replace(/leading-relaxed/g, 'leading-tight');
content = content.replace(/leading-loose/g, 'leading-tight');
content = content.replace(/leading-normal/g, 'leading-tight');
content = content.replace(/leading-8/g, 'leading-tight');
content = content.replace(/leading-7/g, 'leading-tight');
content = content.replace(/leading-6/g, 'leading-tight');

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
