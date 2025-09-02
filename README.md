# Django MSSQL 로그인 시스템

Django와 MSSQL을 연동한 사용자 인증 및 로그인 시스템입니다.

## 주요 기능

- ✅ 사용자 회원가입/로그인/로그아웃
- ✅ 사용자 프로필 관리 (전화번호, 주소 등)
- ✅ Bootstrap5 기반 반응형 UI
- ✅ Django Crispy Forms를 활용한 폼 스타일링
- ✅ MSSQL 데이터베이스 연동
- ✅ Django Admin 연동

## 기술 스택

- **Backend**: Django 5.2.5
- **Database**: Microsoft SQL Server
- **Frontend**: Bootstrap 5, Font Awesome
- **Forms**: Django Crispy Forms
- **Database Driver**: pyodbc

## 설치 및 설정

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. MSSQL 데이터베이스 설정
`login_project/settings.py`에서 데이터베이스 정보를 수정하세요:

```python
DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'YourDatabaseName',      # MSSQL 데이터베이스 이름
        'USER': 'YourUsername',          # MSSQL 사용자명
        'PASSWORD': 'YourPassword',      # MSSQL 비밀번호
        'HOST': 'localhost',             # MSSQL 서버 주소
        'PORT': '1433',                 # MSSQL 포트
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
    }
}
```

### 3. 데이터베이스 마이그레이션
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. 슈퍼유저 생성
```bash
python manage.py createsuperuser
```

### 5. 개발 서버 실행
```bash
python manage.py runserver
```

## 프로젝트 구조

```
Django-Sample/
├── accounts/                 # 사용자 인증 앱
│   ├── models.py           # 사용자 프로필 모델
│   ├── views.py            # 뷰 로직
│   ├── forms.py            # 폼 클래스
│   ├── urls.py             # URL 패턴
│   └── admin.py            # Admin 설정
├── login_project/           # 메인 프로젝트
│   ├── settings.py         # 프로젝트 설정
│   └── urls.py             # 메인 URL 설정
├── templates/               # HTML 템플릿
│   ├── base.html           # 기본 템플릿
│   └── accounts/           # 계정 관련 템플릿
│       ├── login.html      # 로그인 페이지
│       ├── register.html   # 회원가입 페이지
│       ├── home.html       # 홈 페이지
│       └── profile.html    # 프로필 페이지
├── static/                  # 정적 파일
├── manage.py               # Django 관리 스크립트
└── README.md               # 프로젝트 설명서
```

## 사용법

1. **회원가입**: `/register/` 페이지에서 새 계정 생성
2. **로그인**: `/login/` 페이지에서 계정으로 로그인
3. **홈**: 로그인 후 메인 페이지로 이동
4. **프로필**: 사용자 정보 확인 및 관리
5. **로그아웃**: 안전한 로그아웃

## 주의사항

- MSSQL ODBC Driver 17 이상이 설치되어 있어야 합니다
- 데이터베이스 연결 정보는 보안을 위해 환경변수로 관리하는 것을 권장합니다
- 프로덕션 환경에서는 `DEBUG = False`로 설정하세요

## 라이선스

MIT License
