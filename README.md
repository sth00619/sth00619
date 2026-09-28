<div align="center">

<h3><code>song@github ~ $ ./contributions.sh</code></h3>

<img src="./contrib-heatmap.svg" width="860" />

<br><br>

<h3><code>song@github ~ $ whoami</code></h3>

<table>
  <tr>
    <td valign="top"><img src="./avi-ascii.svg" width="370" /></td>
    <td valign="top"><img src="./info-card.svg" width="480" /></td>
  </tr>
</table>

</div>

---

<h3><code>song@github ~ $ cat portfolio.md</code></h3>

### 🔍 WO Series — AI Engineering

> 평가 없이 만든 것은 데모입니다. 모든 프로젝트는 **Eval · Number · Tradeoff** 세 가지를 갖춰야 완료로 인정합니다.

| # | 프로젝트 | 핵심 결과 | 스택 | 상태 |
|---|---|---|---|:---:|
| [WO-01](https://github.com/sth00619/Personal-Portfolio/tree/main/projects/wo-01-retrieval-eval) | 검색 평가 하네스 | Recall@10 **0.8244** · CI regression gate | BM25 · FAISS · pytrec_eval · pytest | ✅ |
| [WO-02](https://github.com/sth00619/Personal-Portfolio/tree/main/projects/wo-02-hybrid-rag) | 하이브리드 RAG | BM25 대비 Recall **+6.69%p** · Faithfulness 0.5667 | RRF · NLI · sentence-transformers | ✅ |
| [WO-03](https://github.com/sth00619/Personal-Portfolio/tree/main/projects/wo-03-semantic-cache) | 시맨틱 캐시 | False-hit **0/9** · 비용 67.5%↓(모델링) | Redis · FAISS · quora-distilbert | ✅ |
| WO-04 | 멀티에이전트 오케스트레이션 | 종료 조건 · 체크포인트 · HITL | LangGraph · Redis · OpenTelemetry | 🔄 |
| WO-05 | 프롬프트 인젝션 가드레일 | 공격 성공률 전후 비교 · 레이어드 방어 | sqlglot · guard model | ⬜ |
| WO-06 | 신용평가 스코어카드 | Gini stability · PSI 모니터링 | optbinning · LightGBM · SHAP | ⬜ |

<details>
<summary>WO-07~24 · 확장 배치 보기</summary>

| # | 프로젝트 | 직군 | 상태 |
|---|---|---|:---:|
| WO-07 | 광고 CTR 예측 & 캘리브레이션 | ML Engineer (광고) | ⬜ |
| WO-08 | RTB 입찰 전략 & 예산 페이싱 | ML Engineer (광고) | ⬜ |
| WO-09 | 2단 추천 + 반사실 평가 (OPE) | ML Engineer (추천) | ⬜ |
| WO-10 | 프로모션 Uplift 타겟팅 | DS (인과추론) | ⬜ |
| WO-11 | 배달 배차 OR 시뮬레이터 ⭐ | ML/OR DS | ⬜ |
| WO-12 | 수요·ETA 분위수 예측 | DS (예측) | ⬜ |
| WO-13 | 실시간 사기탐지 | DS · MLE | ⬜ |
| WO-14 | 신용평가 안정성 | 금융 DS | ⬜ |
| WO-15 | 코호트·리텐션 분석 | 데이터 분석가 | ⬜ |
| WO-16 | Text-to-SQL + 가드레일 | AI Agent | ⬜ |
| WO-17 | 하이브리드 검색 LTR | ML Engineer (검색) | ⬜ |
| WO-18 | LLM 게이트웨이 ⭐ | AI 백엔드 | ⬜ |
| WO-19 | 모델 회귀 탐지 | MLOps | ⬜ |
| WO-20 | 프롬프트 A/B 플랫폼 | AI Engineer | ⬜ |
| WO-21 | 멀티모달 문서 처리 | AI Engineer | ⬜ |
| WO-22 | LLM 비용 오토파일럿 | AI Engineer | ⬜ |
| WO-23 | 공시 레이크하우스 ⭐ | 데이터 엔지니어 | ⬜ |
| WO-24 | 포트폴리오 백테스트 | 금융 DS | ⬜ |

⭐ 산업공학 OR · 백엔드 2년 · 금융 API 경험 직결

</details>

---

### 📊 Data Profolio — 데이터 분석·엔지니어링

| # | 프로젝트 | 핵심 스택 | 상태 |
|---|---|---|:---:|
| P1 | 실시간 금융 거래 이상탐지 대시보드 | XGBoost · Airflow · FastAPI · Redis | ⬜ |
| P2 | SaaS 고객 이탈 예측 및 코호트 분석 | LightGBM · SHAP · dbt · Spring Boot | ⬜ |
| P3 | 서울 대중교통 지연 예측 및 경로 최적화 | PostGIS · TimescaleDB · LSTM · Mapbox | ⬜ |
| P4 | K-뷰티 글로벌 트렌드 분석 및 수요 예측 | pytrends · ES · Prophet | ⬜ |
| P5 | 서울 상권 분석 및 점포 입지 추천 | H3 · PostGIS · Deck.gl · LightGBM | ⬜ |
| P6 | 글로벌 지역·산업 인텔리전스 플랫폼 | Mapbox Globe · Deck.gl · PostGIS | ⬜ |
| P7M | 이커머스 그로스 마케팅 성과 분석 | GA4 · RFM · ROAS · FastAPI | ⬜ |
| P7P | SaaS 프로덕트 분석 및 기능 개선 | Aha Moment · RICE · dbt | ⬜ |

---

### 📚 학습 트랙

| 트랙 | 내용 | 진행 |
|---|---|---|
| **B · 금융·수학** | 확률통계 (MIT 6.041SC · Stat110 · CS109) · 선형대수 (MIT 18.06→18.065) · DS/ML (ISLP→CS229) | §1~3 완료 |
| **C · 에이전트·Harness** | ReAct · 워크플로 5패턴 · CoALA 메모리 · MCP · SWE-bench · τ-bench | 준비 완료 |
| **D · SQL·DB** | CMU 15-445 · PostgreSQL Exercises · DataLemur · 차원 모델링 (Kimball) · dbt | 진행 중 |

---

### 🔗 Links

[![Notion Portfolio Hub](https://img.shields.io/badge/Notion-Portfolio_Hub-black?style=flat-square&logo=notion&logoColor=white)](https://app.notion.com/p/3df76d2e4c1c80b1b168db16c30a457d)
[![Personal Portfolio Repo](https://img.shields.io/badge/GitHub-Personal--Portfolio-181717?style=flat-square&logo=github)](https://github.com/sth00619/Personal-Portfolio)
[![Portfolio Site](https://img.shields.io/badge/Site-sth00619.github.io-0078D4?style=flat-square&logo=githubpages)](https://sth00619.github.io/Personal-Portfolio/)
