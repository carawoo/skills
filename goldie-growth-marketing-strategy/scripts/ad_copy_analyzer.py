#!/usr/bin/env python3
"""
Meta Ads Copy Analyzer
카피를 7가지 심리학적 카테고리로 분류 및 점수 매기기
"""

import json
from typing import Dict, List, Tuple

class AdCopyAnalyzer:
    def __init__(self):
        # 7가지 심리학적 카테고리 정의
        self.categories = {
            "숫자형": {
                "keywords": ["매일", "하루", "월", "1,000원", "1분", "일일", "매달"],
                "psychology": "구체적 수치로 즉각성 강조",
                "effectiveness": 8.5,
                "compliance_risk": 2,
                "target": "20-35세"
            },
            "비교형": {
                "keywords": ["포인트 말고", "대신", "vs", "비교", "차별", "다르게"],
                "psychology": "손실 회피, 명확한 차별성",
                "effectiveness": 8.2,
                "compliance_risk": 1,
                "target": "25-40세"
            },
            "무자본형": {
                "keywords": ["무자본", "0원", "돈 없이", "무료", "시작", "부담 없이"],
                "psychology": "진입장벽 제거",
                "effectiveness": 8.0,
                "compliance_risk": 1,
                "target": "20-35세"
            },
            "실험형": {
                "keywords": ["실험", "해봤", "30일", "직접", "확인", "검증"],
                "psychology": "신뢰성 검증, 직접 경험",
                "effectiveness": 7.8,
                "compliance_risk": 1,
                "target": "25-40세"
            },
            "루틴형": {
                "keywords": ["출석", "매일", "습관", "집에서", "커피", "조금씩"],
                "psychology": "게임화, 최소 행동",
                "effectiveness": 7.5,
                "compliance_risk": 0,
                "target": "20-35세"
            },
            "컨텐츠형": {
                "keywords": ["요즘", "써보는", "발견", "많이 해봤", "신기함", "처음"],
                "psychology": "사회적 증명, UGC 스타일",
                "effectiveness": 7.3,
                "compliance_risk": 0,
                "target": "20-35세"
            },
            "사회적증거형": {
                "keywords": ["다들", "많은", "요즘", "사람", "주변", "시작했"],
                "psychology": "FOMO, 시대 흐름",
                "effectiveness": 7.0,
                "compliance_risk": 1,
                "target": "25-45세"
            }
        }

    def classify_copy(self, copy: str) -> Tuple[str, float]:
        """카피를 카테고리로 분류"""
        max_score = 0
        best_category = "기타"
        
        for category, info in self.categories.items():
            score = 0
            for keyword in info["keywords"]:
                if keyword in copy:
                    score += 1
            
            if score > max_score:
                max_score = score
                best_category = category
        
        confidence = min(max_score / 3, 1.0)  # 최대 3개 키워드 기준
        return best_category, confidence

    def calculate_effectiveness_score(self, category: str, copy: str) -> float:
        """효과성 점수 계산"""
        base_score = self.categories[category]["effectiveness"]
        
        # 길이 보너스 (30-50자 최적)
        if 30 <= len(copy) <= 50:
            base_score += 0.5
        
        # 숫자 포함 보너스
        if any(char.isdigit() for char in copy):
            base_score += 0.3
        
        return min(base_score, 10.0)

    def calculate_compliance_risk(self, category: str) -> int:
        """규제 리스크 점수"""
        return self.categories[category]["compliance_risk"]

    def calculate_brand_fit(self, copy: str, brand_tone: str = "친근한 전문가") -> float:
        """브랜드 정합성 점수"""
        score = 7.0
        
        # 친근한 전문가 톤에 맞는 표현
        friendly_words = ["조금씩", "매일", "습관", "쉽게", "재미"]
        professional_words = ["신뢰", "검증", "안정", "공정", "투명"]
        
        friendly_count = sum(1 for word in friendly_words if word in copy)
        professional_count = sum(1 for word in professional_words if word in copy)
        
        score += friendly_count * 0.5
        score += professional_count * 0.5
        
        return min(score, 10.0)

    def calculate_overall_score(self, 
                               effectiveness: float,
                               compliance_risk: int,
                               brand_fit: float) -> float:
        """종합 점수 계산"""
        # 가중치: 효과성 40%, 규제 리스크 30%, 브랜드 정합성 30%
        risk_score = 10 - (compliance_risk * 2)  # 리스크를 점수로 변환
        
        overall = (effectiveness * 0.4) + (risk_score * 0.3) + (brand_fit * 0.3)
        return round(overall, 1)

    def analyze_copy(self, copy: str, brand_tone: str = "친근한 전문가") -> Dict:
        """카피 전체 분석"""
        category, confidence = self.classify_copy(copy)
        effectiveness = self.calculate_effectiveness_score(category, copy)
        compliance_risk = self.calculate_compliance_risk(category)
        brand_fit = self.calculate_brand_fit(copy, brand_tone)
        overall_score = self.calculate_overall_score(effectiveness, compliance_risk, brand_fit)
        
        return {
            "copy": copy,
            "category": category,
            "confidence": round(confidence, 2),
            "effectiveness_score": round(effectiveness, 1),
            "compliance_risk": compliance_risk,
            "compliance_level": self._get_compliance_level(compliance_risk),
            "brand_fit": round(brand_fit, 1),
            "overall_score": overall_score,
            "psychology": self.categories[category]["psychology"],
            "target": self.categories[category]["target"],
            "recommendation": self._get_recommendation(overall_score)
        }

    def _get_compliance_level(self, risk: int) -> str:
        """규제 리스크 레벨"""
        if risk == 0:
            return "✅ 낮음"
        elif risk == 1:
            return "⚠️ 중간"
        else:
            return "🚨 높음"

    def _get_recommendation(self, score: float) -> str:
        """추천 등급"""
        if score >= 8.5:
            return "🌟 1순위 (필수)"
        elif score >= 8.0:
            return "⭐ 1순위 (강력 추천)"
        elif score >= 7.5:
            return "👍 2순위 (권장)"
        elif score >= 7.0:
            return "👌 3순위 (선택)"
        else:
            return "❌ 개선 필요"

    def analyze_multiple_copies(self, copies: List[str], 
                               brand_tone: str = "친근한 전문가") -> List[Dict]:
        """여러 카피 분석"""
        results = []
        for copy in copies:
            results.append(self.analyze_copy(copy, brand_tone))
        
        # 점수순 정렬
        results.sort(key=lambda x: x["overall_score"], reverse=True)
        return results

    def get_top_copies(self, copies: List[str], top_n: int = 10) -> List[Dict]:
        """상위 N개 카피 추출"""
        results = self.analyze_multiple_copies(copies)
        return results[:top_n]

    def get_category_distribution(self, copies: List[str]) -> Dict[str, int]:
        """카테고리별 분포"""
        distribution = {cat: 0 for cat in self.categories.keys()}
        
        for copy in copies:
            category, _ = self.classify_copy(copy)
            distribution[category] += 1
        
        return distribution


def main():
    """테스트 실행"""
    analyzer = AdCopyAnalyzer()
    
    test_copies = [
        "매일 금 1,000원 모으기",
        "포인트는 사라지지만 금은 남습니다",
        "하루 1분 금 모으기",
        "무자본 금 앱테크",
        "30일 동안 금 모아봤더니",
        "요즘 금 모으는 앱 써보는 중",
        "다들 금 모으기 시작했다는데"
    ]
    
    results = analyzer.analyze_multiple_copies(test_copies)
    
    print("=" * 100)
    print("Meta Ads Copy Analysis Results")
    print("=" * 100)
    
    for i, result in enumerate(results, 1):
        print(f"\n{i}. {result['copy']}")
        print(f"   분류: {result['category']} (신뢰도: {result['confidence']*100:.0f}%)")
        print(f"   종합점수: {result['overall_score']}/10 {result['recommendation']}")
        print(f"   - 효과성: {result['effectiveness_score']}/10")
        print(f"   - 규제리스크: {result['compliance_level']}")
        print(f"   - 브랜드정합: {result['brand_fit']}/10")
        print(f"   심리학: {result['psychology']}")
        print(f"   타겟: {result['target']}")


if __name__ == "__main__":
    main()
