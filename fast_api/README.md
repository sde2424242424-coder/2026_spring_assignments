# FastAPI Basic Guide

This project demonstrates core FastAPI concepts in a simple and structured way.

---

## Installation

Install FastAPI and run the server.

Docs:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

---

## 1. First Steps

Basic FastAPI application with a simple endpoint that returns data.

---

## 2. Path Parameters

Parameters included in the URL path, used to identify specific resources.

Note: Route order is important.

---

## 3. Query Parameters

Optional parameters passed after `?` in the URL.

Feature: Automatic type conversion (int, bool, etc.)

---

## 4. Request Body

Used to send JSON data from client to server (POST, PUT).

Feature: Automatic validation using Pydantic.

---

## 5. Path Parameters and Numeric Validations

Numeric constraints can be applied (greater than, less than, etc.).

Result: Invalid values automatically return errors.

---

## 6. Query Parameter Models

Multiple query parameters can be grouped into a single model.

Benefit: Cleaner structure and reusability.

---

## Summary

FastAPI uses Python type hints to:
- validate input data  
- convert types automatically  
- generate API documentation  

---

# FastAPI 기본 가이드

이 프로젝트는 FastAPI의 핵심 개념을 간단하고 구조적으로 설명합니다.

---

## 설치

FastAPI를 설치하고 서버를 실행합니다.

문서:
- http://127.0.0.1:8000/docs
- http://127.0.0.1:8000/redoc

---

## 1. First Steps

기본 FastAPI 애플리케이션과 간단한 데이터 반환 엔드포인트.

---

## 2. Path Parameters

URL 경로에 포함된 값으로 특정 리소스를 식별합니다.

주의: 경로 선언 순서가 중요합니다.

---

## 3. Query Parameters

URL의 `?` 뒤에 전달되는 선택적 파라미터입니다.

특징: 타입 자동 변환 (int, bool 등)

---

## 4. Request Body

클라이언트가 서버로 JSON 데이터를 보낼 때 사용됩니다 (POST, PUT).

특징: Pydantic 기반 자동 데이터 검증

---

## 5. Path Parameters and Numeric Validations

숫자 값에 대해 범위 제한을 설정할 수 있습니다.

결과: 잘못된 값은 자동으로 오류를 반환합니다.

---

## 6. Query Parameter Models

여러 query 파라미터를 하나의 모델로 그룹화할 수 있습니다.

장점: 코드 구조 개선 및 재사용성 향상

---

## 요약

FastAPI는 Python 타입 힌트를 사용하여:
- 데이터 검증  
- 자동 타입 변환  
- API 문서 자동 생성  
을 수행합니다.