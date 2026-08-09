const fs = require('fs');
const filePath = 'C:/AIprojects/roaddata/hubei/release/project/20260808.html';
let content = fs.readFileSync(filePath, 'utf8');

content = content.replace(/<span class="[^"]+">招标文件技术规范<\/span>/g, '');
content = content.replace(/<span class="[^"]+">评估标准规范<\/span>/g, '');
content = content.replace(/<span class="[^"]+">实施方案<\/span>/g, ''); // just in case

fs.writeFileSync(filePath, content, 'utf8');
console.log("Success");
