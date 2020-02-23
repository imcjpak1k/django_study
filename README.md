# django_study
장고스터디

[MarkDown Syntax](https://simhyejin.github.io/2016/06/30/Markdown-syntax/ "MarkDown Syntax")

# vscode settings
```json
{
    "python.pythonPath": "c:\\Users\\imcjp\\venv\\twoscoopsofdjango\\Scripts\\python.exe"
}
```


* django install
  * [https://doorbw.tistory.com/181](https://doorbw.tistory.com/181 "장고설치가이드")
  * [https://docs.djangoproject.com/ko/3.0/intro/install](https://docs.djangoproject.com/ko/3.0/intro/install/ "장고설치가이드")
  * [https://blog.naver.com/imcjpak1k](https://blog.naver.com/imcjpak1k "장고설치가이드")


# django install
> pip install Django

# 프로젝생성
> django-admin startproject {프로젝트명}
> 

# 앱생성
> django-admin startapp {앱이름}
> 

# 서버실행
> manage.py runserver


# requirements
> 설치하지고 하는 라이브러리들에 대한 정보를 파일에 저장 후 한번에 설치도 가능하다.
> 프로젝트 진행 중 추가 또는 삭제되는 라이브러리 정보 및 로컬, 개발, 운영서버에 설치되는 버전정보를
> 파일별로 관리 후 한번에 설치할 수 있다.
> 특히, 로컬개발의 경우에는 설치파일을 공유함으로써 쉽고 편하게 동일한 라이브러리를 설치할 수 있으므로
> 프로젝트를 관리하는 차원에서 좋은 방법이다.
> 
> pip install -r requirements/local.txt
> ```txt
> Django==3.0.3
> ```