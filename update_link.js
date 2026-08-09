const fs = require('fs');
const path = 'C:/AIprojects/roaddata/hubei/release/index.html';
let content = fs.readFileSync(path, 'utf8');

const searchString = 'href: "./project/%E6%B9%96%E5%8C%97%E5%85%AC%E8%B7%AF%E6%95%B0%E6%8D%AE%E6%B2%BB%E7%90%86%E4%B8%93%E9%A1%B9%E8%BF%9B%E5%B1%95%E6%B1%87%E6%8A%A520260808.html"';
const replacementString = 'href: "./project/20260808.html"';

if(content.includes(searchString)) {
    content = content.replace(searchString, replacementString);
    fs.writeFileSync(path, content, 'utf8');
    console.log("Success");
} else {
    console.log("Search string not found!");
}
