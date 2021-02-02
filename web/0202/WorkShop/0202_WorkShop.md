# 0202_WorkShop

### 1. Semantic Tag

- 제시된 semantic.html과 semantic.css를 수정하여 다음 이미지와 같은 형태가 되도록 코드를 작성하시오.

![image-20210202112804660](C:\Users\USER\AppData\Roaming\Typora\typora-user-images\image-20210202112804660.png)

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="semantic.css">
  <title>Layout Practice</title>
</head>
<body>
  <header class="header">
    <h1 class="h1">header</h1>
  </header>
  <nav class="nav">
    <h2>nav</h2>
  </nav>
  <section class="section">
    <h2>section</h2>
    <article class="article">
      <h3>article1</h3>
      <h3>article2</h3>
    </article>
  </section>
  <aside class="aside">
    <h2>aside</h2>
  </aside>
  <footer class="footer">
    <h2>footer</h2>
  </footer>
</body>
</html>

```

```css
body {
  font-family: Arial;
  width: 800px;
}

/* 모든 스타일링 요소를 클래스로 만들어 사용합니다. */

/* 1. article 태그는 white로 나머지 시멘틱 태그는 lightgrey로 배경색을 바꿔주세요. */
.header, .nav, .section, .aside, .footer {
  background-color: lightgrey;
}
.article {
  background-color: white;
}
/* 2. 모든 시멘틱 태그의 margin과 padding을 4px로 만들어주세요. */
.header, .nav, .section, .aside, .footer, .article {
  margin: 4px;
  padding: 4px;
}
/* 3. h1 태그를 중앙 정렬 시켜주세요. */
.h1 {
  text-align: center;
}
/* 4. section과 aside 태그의 display를 inline-block으로 바꿔주세요. */
.section, .aside {
  display: inline-block;
}
/* 5. section 태그는 width 482px height 300px, aside 태그는 width 280px height 300px로 만들어주세요.*/
.section {
  width: 482px;
  height: 300px;
}
.aside {
  width: 280px;
  height: 300px;
}
/* 6. aside 태그에 vertical-align속성의 값을 top으로 적용해주세요.*/
.aside {
  vertical-align: top;
}
/* 7. 모든 semantic 태그의 border 모서리 반경을 4px로 만들어주세요. */
.header, .nav, .section, .aside, .footer, .article {
  border-radius: 4px;
}
```

