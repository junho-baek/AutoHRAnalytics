# Poetry 사용법 (Windows PowerShell)

## 1. Poetry 설치

PowerShell을 관리자 권한으로 실행 후 아래 명령어 입력:

```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

## 2. 프로젝트 생성 및 설정

### 2.1 새 프로젝트 생성

```
poetry new 프로젝트이름
```

### 2.2 기존 프로젝트에 Poetry 추가

프로젝트 폴더에서:

```
poetry init
```

## 3. 의존성 관리

### 3.1 패키지 설치

```
poetry add 패키지이름
```

### 3.2 개발용 패키지 설치

```
poetry add --dev 패키지이름
```

### 3.3 모든 의존성 설치

```
poetry install
```

## 4. 가상환경 관리

### 4.1 가상환경 생성 및 활성화

```

poetry env use python

```

### 4.2 가상환경 비활성화

```
exit
```

## 5. 스크립트 실행

### 5.1 Python 스크립트 실행

```
poetry run python 스크립트.py
```

### 5.2 다른 명령어 실행

```
poetry run 명령어
```

## 6. 의존성 업데이트

### 6.1 모든 패키지 업데이트

```
poetry update
```

### 6.2 특정 패키지 업데이트

```
poetry update 패키지이름
```

## 7. 프로젝트 빌드 및 배포

### 7.1 프로젝트 빌드

```
poetry build
```

### 7.2 PyPI에 배포

```
poetry publish
```
