#!/usr/bin/env python3
"""
Meta Ads Copy Compliance Checker
금융감독청(FSC), 공정거래위원회(FTC) 기준 자동 검사
"""

import json
import re
from typing import Dict, List, Tuple

class CopyComplianceChecker:
    def __init__(self):
        # 절대적 표현 패턴
        self.absolute_patterns = [
            r'최고', r'가장', r'최상', r'최고의', r'최고급',
            r'최고가', r'최저가', r'절대', r'무조건', r'반드시'
        ]
        
        # 수익 보장 패턴
        self.profit_guarantee_patterns = [
            r'월\s*\d+만원\s*(이상|이하)',
            r'일\s*\d+원',
            r'수익\s*보장',
            r'확정\s*수익',
            r'보장\s*수익',
            r'수익률\s*\d+%'
        ]
        
        # 손실 미표시 패턴
        self.loss_omission_patterns = [
            r'손실\s*없음',
            r'위험\s*없음',
            r'안전\s*100%',
            r'절대\s*손실\s*없음'
        ]
        
        # 근거 부족 패턴
        self.unsubstantiated_patterns = [
            r'대부분', r'많은 사람', r'인기', r'트렌드',
            r'화제', r'유명', r'유행'
        ]

    def check_absolute_expressions(self, copy: str) -> Tuple[bool, str]:
        """절대적 표현 검사"""
        for pattern in self.absolute_patterns:
            if re.search(pattern, copy):
                return True, f"절대적 표현 감지: '{pattern}' - 금지됨"
        return False, ""

    def check_profit_guarantee(self, copy: str) -> Tuple[bool, str]:
        """수익 보장 표현 검사"""
        for pattern in self.profit_guarantee_patterns:
            if re.search(pattern, copy):
                return True, f"수익 보장 표현 감지: 근거 데이터 필수"
        return False, ""

    def check_loss_omission(self, copy: str) -> Tuple[bool, str]:
        """손실 미표시 검사"""
        for pattern in self.loss_omission_patterns:
            if re.search(pattern, copy):
                return True, f"손실 미표시 감지: 위험 고지 필수"
        return False, ""

    def check_unsubstantiated_claims(self, copy: str) -> Tuple[bool, str]:
        """근거 부족 표현 검사"""
        for pattern in self.unsubstantiated_patterns:
            if re.search(pattern, copy):
                return True, f"근거 부족 표현 감지: '{pattern}' - 근거 필수"
        return False, ""

    def get_risk_score(self, copy: str) -> int:
        """규제 리스크 점수 계산 (0-10)"""
        score = 0
        
        # 각 검사별 점수
        if self.check_absolute_expressions(copy)[0]:
            score += 3
        if self.check_profit_guarantee(copy)[0]:
            score += 4
        if self.check_loss_omission(copy)[0]:
            score += 2
        if self.check_unsubstantiated_claims(copy)[0]:
            score += 1
        
        return min(score, 10)

    def get_improvement_suggestion(self, copy: str, risk_score: int) -> str:
        """개선안 제시"""
        suggestions = []
        
        if self.check_absolute_expressions(copy)[0]:
            suggestions.append("→ 절대적 표현 제거 (예: '최고' → '공정한')")
        
        if self.check_profit_guarantee(copy)[0]:
            suggestions.append("→ 구체적 수익 표현 제거 또는 근거 데이터 첨부")
        
        if self.check_loss_omission(copy)[0]:
            suggestions.append("→ 위험 고지 추가 (예: '손실 가능성 있음')")
        
        if self.check_unsubstantiated_claims(copy)[0]:
            suggestions.append("→ 근거 데이터 첨부 또는 표현 수정")
        
        if risk_score == 0:
            suggestions.append("✅ 규제 리스크 없음 - 승인 가능")
        
        return "\n".join(suggestions)

    def check_copy(self, copy: str) -> Dict:
        """카피 전체 검사"""
        risk_score = self.get_risk_score(copy)
        
        return {
            "copy": copy,
            "risk_score": risk_score,
            "risk_level": self._get_risk_level(risk_score),
            "absolute_expression": self.check_absolute_expressions(copy)[1],
            "profit_guarantee": self.check_profit_guarantee(copy)[1],
            "loss_omission": self.check_loss_omission(copy)[1],
            "unsubstantiated": self.check_unsubstantiated_claims(copy)[1],
            "improvement": self.get_improvement_suggestion(copy, risk_score)
        }

    def _get_risk_level(self, score: int) -> str:
        """리스크 레벨 판정"""
        if score == 0:
            return "✅ 낮음"
        elif score <= 3:
            return "⚠️ 중간"
        else:
            return "🚨 높음"

    def check_multiple_copies(self, copies: List[str]) -> List[Dict]:
        """여러 카피 검사"""
        results = []
        for copy in copies:
            results.append(self.check_copy(copy))
        return results


def main():
    """테스트 실행"""
    checker = CopyComplianceChecker()
    
    test_copies = [
        "매일 금 1,000원 모으기",
        "포인트는 사라지지만 금은 남습니다",
        "월 10만원 이상 가능한 비결",
        "최고가로 금을 사드립니다",
        "위험 없이 금을 모으세요"
    ]
    
    results = checker.check_multiple_copies(test_copies)
    
    print("=" * 80)
    print("Meta Ads Copy Compliance Check Results")
    print("=" * 80)
    
    for result in results:
        print(f"\n📝 Copy: {result['copy']}")
        print(f"   Risk Score: {result['risk_score']}/10 ({result['risk_level']})")
        if result['absolute_expression']:
            print(f"   ⚠️ {result['absolute_expression']}")
        if result['profit_guarantee']:
            print(f"   ⚠️ {result['profit_guarantee']}")
        if result['loss_omission']:
            print(f"   ⚠️ {result['loss_omission']}")
        if result['unsubstantiated']:
            print(f"   ⚠️ {result['unsubstantiated']}")
        print(f"\n   💡 개선안:\n{result['improvement']}")
        print("-" * 80)


if __name__ == "__main__":
    main()
