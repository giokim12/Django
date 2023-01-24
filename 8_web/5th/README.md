# Project 03

## 1. Navigation Bar 구현

### __<스크롤을 하더라도 항상 화면 상단/하단에 고정>__
Fixed: 스크롤해도 움직이지 않음  
Sticky: 상위 요소에 달라 붙음. 콘텐츠마다 고정해야 하는 내용이 달라지는 경우에는 sticky 사용.  
https://ordinary-code.tistory.com/106

### __<로고 이미지에 링크>__
```html
    <a class="navbar-brand" href="02_home.html">
      <img src="logo.png" alt="" width="120" height="50" class="d-inline-block align-text-top">
    </a>
```
이미지를 감싸고 있는 `<a></a>`에 href=""를 넣어준다.

### __<모달 컴포넌트 구현>__
https://getbootstrap.com/docs/5.2/components/modal/#varying-modal-content

1. 먼저, navbar에 있는 로그인을 클릭했을 때 모달이 뜨게끔 설정을 해야한다. 
```html
        <li class="nav-item mx-3">
          <a class="nav-link" data-bs-toggle="modal" data-bs-target="#exampleModal">Login</a>
        </li>
```
navbar안에 로그인 글자가 들어가는 곳에, 모달을 넣어주겠다는 toggle과 타켓을 넣는다.
```html
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
```
<small>모달 넣는 첫 줄만 복붙했음</small>  
모달 클래스에 있는 id랑 data-bs-target은 같아야한다! 해시태그(#)도 넣어야함.

2. 모달에 맞는 component 넣기 
* 이메일 주소에 We'll never share your email with anyone else
```html
<div id="emailHelp" class="form-text">We'll never share your email with anyone else</div>
```
이메일 적는 박스 바로 밑에 div를 새로 만들어서 text를 넣어준다.

### __<크기가 768px 미만일때 목록으로 나오게>__

상단바 오른쪽 위에 있는걸 눌러야 페이지 목록이 나오게 하는 거니까 button을 새로 생성해준다.  
이것도 아까 로그인 누르고 모달 나올때랑 마찬가지로,  
버튼 눌렀을 때 목록이 나오게 id를 같게 해줘야 한다. 

```html
<button class="navbar-toggler text-white" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon text-white"></span>
    </button>
<div class="collapse navbar-collapse" id="navbarTogglerDemo01">
    <a class="navbar-brand" href="#"></a>
    <ul class="navbar-nav mb-2 mb-lg-0"> 
    ...
    </ul>
```

___
## 2. Home Page

### __<부트스트랩 카드 컴포넌트 좌우 간격>__
css 사용 안하고 부트스트랩 내에서 하는건,  
그리드에서 margin padding을 생각하면 된다.  
```
mb-3
```
꼭 넣기

### __<크기 576 이상/이하일때 한 행에 표시되는 개수 바꾸기>__
크기가 576픽셀 이하일때는 한줄에 표시되는 영화 개수가 한개여야 한다.  
한 화면은 가로 12개의 그리드로 이루어져있기 때문에  
픽셀이 576 미만일 때, 길이가 12이다 라고 하면 된다
```html
  <div class="container">
    <section class="row">
      <div class="col col-12 col-sm-4 mb-3">
```
* 그리드는 container, row 가 꼭 필요!!!! 잊지말기

___
## 3. Community Page

### __<리스트 안 글자에 하이퍼링크 넣기>__
```html
<a href="URL" target="#" class="list-group-item list-group-item-action text-primary">Movies</a>
```
URL을 넣을 것이기 때문에 href를 URL로 설정하고,  
글자의 색깔이 파랑색이기 때문에 text-primary를 써준다.  


### __<가로 크기별 보여지는 표 다르게 하기>__
그리드의 크기에 따라 특정 component 가 보여지고 안보여지게 하는건
d-none과 d-block을 사용하면 된다. 
	
https://zetawiki.com/wiki/%EB%B6%80%ED%8A%B8%EC%8A%A4%ED%8A%B8%EB%9E%A94_%EC%88%A8%EA%B9%80_%ED%81%B4%EB%9E%98%EC%8A%A4

```html
<div class="d-lg-block col-lg-10 d-none">
```
코드설명: 창이 992픽셀(large)보다 커지면 내꺼 클래스를 보여주고, 그리드에서 10의 공간을 차지하게 한다. 
아니면 내꺼 클래스를 보이지 않게 한다. 