import os
import openai
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")


class SajuAI:
    def __init__(self):
        # 이전 버전의 OpenAI API 사용
        pass

    def generate_saju_interpretation(self, saju_data: Dict[str, Any]) -> str:
        """
        ChatGPT를 사용하여 사주 해석을 생성합니다.
        """
        try:
            # 사주 데이터를 기반으로 프롬프트 생성
            prompt = self._create_saju_prompt(saju_data)

            # ChatGPT API 호출 (이전 버전)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": """당신은 전문적인 사주 해석가입니다. 
                        한국 전통 사주학에 대한 깊은 지식을 바탕으로 
                        정확하고 유용한 해석을 제공해주세요.
                        
                        해석 시 다음 사항을 고려해주세요:
                        1. 오행의 균형과 조화
                        2. 사주팔자의 전체적인 흐름
                        3. 개인의 성격과 운세
                        4. 실용적인 조언과 방향성
                        
                        답변은 친근하고 이해하기 쉽게 작성해주세요.""",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=800,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"ChatGPT API 오류: {e}")
            return self._get_fallback_interpretation(saju_data)

    def generate_fortune_summary(self, saju_data: Dict[str, Any]) -> str:
        """
        ChatGPT를 사용하여 간단한 운세 요약을 생성합니다.
        """
        try:
            elements = saju_data.get("elements", {})
            prompt = f"""
            다음 오행 분석을 바탕으로 간단하고 긍정적인 운세 요약을 해주세요:
            
            오행 분석:
            - 목(木): {elements.get("wood", 0)}개
            - 화(火): {elements.get("fire", 0)}개
            - 토(土): {elements.get("earth", 0)}개
            - 금(金): {elements.get("metal", 0)}개
            - 수(水): {elements.get("water", 0)}개
            
            위 오행 분석을 바탕으로 1-2문장으로 간단하고 긍정적인 운세 요약을 해주세요.
            너무 길지 않고 핵심만 담아주세요.
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 친근하고 긍정적인 사주 해석가입니다. 간단하고 실용적인 조언을 제공해주세요.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=100,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"Fortune 생성 오류: {e}")
            return self._get_fallback_fortune(saju_data)

    def generate_money_fortune(self, saju_data: Dict[str, Any]) -> str:
        """
        ChatGPT를 사용하여 올해의 금전운을 생성합니다.
        """
        try:
            elements = saju_data.get("elements", {})
            prompt = f"""
            다음 오행 분석을 바탕으로 올해(2025년)의 금전운을 해석해주세요:
            
            오행 분석:
            - 목(木): {elements.get("wood", 0)}개
            - 화(火): {elements.get("fire", 0)}개
            - 토(土): {elements.get("earth", 0)}개
            - 금(金): {elements.get("metal", 0)}개
            - 수(水): {elements.get("water", 0)}개
            
            위 오행 분석을 바탕으로 올해의 금전운을 2-3문장으로 해석해주세요.
            구체적인 조언과 함께 긍정적인 관점에서 설명해주세요.
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 전문적인 사주 해석가입니다. 금전운에 대한 실용적이고 긍정적인 조언을 제공해주세요.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=150,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"금전운 생성 오류: {e}")
            return self._get_fallback_money_fortune(saju_data)

    def generate_love_fortune(self, saju_data: Dict[str, Any]) -> str:
        """
        ChatGPT를 사용하여 올해의 애정운을 생성합니다.
        """
        try:
            elements = saju_data.get("elements", {})
            gender = saju_data.get("birth_info", {}).get("gender", "")
            prompt = f"""
            다음 오행 분석을 바탕으로 올해(2025년)의 애정운을 해석해주세요:
            
            성별: {gender}
            오행 분석:
            - 목(木): {elements.get("wood", 0)}개
            - 화(火): {elements.get("fire", 0)}개
            - 토(土): {elements.get("earth", 0)}개
            - 금(金): {elements.get("metal", 0)}개
            - 수(水): {elements.get("water", 0)}개
            
            위 오행 분석을 바탕으로 올해의 애정운을 2-3문장으로 해석해주세요.
            성별을 고려하여 적절한 조언을 제공해주세요.
            """

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 전문적인 사주 해석가입니다. 애정운에 대한 따뜻하고 실용적인 조언을 제공해주세요.",
                    },
                    {"role": "user", "content": prompt},
                ],
                max_tokens=150,
                temperature=0.7,
            )

            return response.choices[0].message.content

        except Exception as e:
            print(f"애정운 생성 오류: {e}")
            return self._get_fallback_love_fortune(saju_data)

    def _create_saju_prompt(self, saju_data: Dict[str, Any]) -> str:
        """
        사주 데이터를 기반으로 ChatGPT 프롬프트를 생성합니다.
        """
        birth_info = saju_data.get("birth_info", {})
        saju = saju_data.get("saju", {})
        elements = saju_data.get("elements", {})

        prompt = f"""
        다음 사주 정보를 바탕으로 상세한 해석을 해주세요:
        
        생년월일: {birth_info.get("date", "알 수 없음")}
        생시: {birth_info.get("time", "알 수 없음")}
        성별: {birth_info.get("gender", "알 수 없음")}
        
        사주팔자:
        - 년주: {saju.get("year_pillar", "알 수 없음")}
        - 월주: {saju.get("month_pillar", "알 수 없음")}
        - 일주: {saju.get("day_pillar", "알 수 없음")}
        - 시주: {saju.get("hour_pillar", "알 수 없음")}
        
        오행 분석:
        - 목(木): {elements.get("wood", 0)}개
        - 화(火): {elements.get("fire", 0)}개
        - 토(土): {elements.get("earth", 0)}개
        - 금(金): {elements.get("metal", 0)}개
        - 수(水): {elements.get("water", 0)}개
        
        다음 항목에 대해 상세히 해석해주세요:
        1. 전체적인 사주의 특징
        2. 성격 분석
        3. 직업과 재물운
        4. 건강과 관계운
        5. 올해의 운세와 조언
        
        답변은 3-4문단으로 구성하여 친근하고 실용적으로 작성해주세요.
        """

        return prompt

    def _get_fallback_interpretation(self, saju_data: Dict[str, Any]) -> str:
        """
        ChatGPT API 오류 시 기본 해석을 제공합니다.
        """
        elements = saju_data.get("elements", {})

        # 오행 균형 분석
        total_elements = sum(elements.values())
        if total_elements == 0:
            return "사주 정보를 분석할 수 없습니다. 다시 시도해주세요."

        # 가장 많은 오행 찾기
        dominant_element = max(elements, key=elements.get)
        element_names = {
            "wood": "목(木)",
            "fire": "화(火)",
            "earth": "토(土)",
            "metal": "금(金)",
            "water": "수(水)",
        }

        interpretations = {
            "wood": "목(木)의 기운이 강한 사주입니다. 창의적이고 성장 지향적인 성격을 가지고 있으며, 새로운 도전을 즐기는 편입니다. 교육, 출판, 환경 관련 분야에서 성공할 가능성이 높습니다.",
            "fire": "화(火)의 기운이 강한 사주입니다. 열정적이고 리더십이 뛰어나며, 사람들을 이끄는 능력이 있습니다. 예술, 엔터테인먼트, 요리 관련 분야에서 재능을 발휘할 수 있습니다.",
            "earth": "토(土)의 기운이 강한 사주입니다. 안정적이고 신뢰할 수 있는 성격으로, 실용적인 사고를 가지고 있습니다. 부동산, 건설, 농업 관련 분야에서 성공할 가능성이 높습니다.",
            "metal": "금(金)의 기운이 강한 사주입니다. 정직하고 원칙적인 성격으로, 조직과 규율을 중시합니다. 금융, 법무, IT 관련 분야에서 능력을 발휘할 수 있습니다.",
            "water": "수(水)의 기운이 강한 사주입니다. 지혜롭고 직관력이 뛰어나며, 유연한 사고를 가지고 있습니다. 연구, 상담, 해외무역 관련 분야에서 성공할 가능성이 높습니다.",
        }

        return interpretations.get(
            dominant_element, "사주를 분석하는 중입니다. 잠시 후 다시 시도해주세요."
        )

    def _get_fallback_fortune(self, saju_data: Dict[str, Any]) -> str:
        """
        Fortune 생성 실패 시 기본 운세를 제공합니다.
        """
        elements = saju_data.get("elements", {})
        total_elements = sum(elements.values())

        if total_elements == 0:
            return "운세를 분석할 수 없습니다."

        dominant_element = max(elements, key=elements.get)

        fortunes = {
            "wood": "목(木)의 기운이 강해 창의적이고 성장하는 한 해가 될 것입니다.",
            "fire": "화(火)의 기운이 강해 열정적이고 활기찬 한 해가 될 것입니다.",
            "earth": "토(土)의 기운이 강해 안정적이고 신뢰받는 한 해가 될 것입니다.",
            "metal": "금(金)의 기운이 강해 정직하고 원칙적인 한 해가 될 것입니다.",
            "water": "수(水)의 기운이 강해 지혜롭고 유연한 한 해가 될 것입니다.",
        }

        return fortunes.get(
            dominant_element, "오행이 균형잡혀 있어 안정적인 운세입니다."
        )

    def _get_fallback_money_fortune(self, saju_data: Dict[str, Any]) -> str:
        """
        금전운 생성 실패 시 기본 금전운을 제공합니다.
        """
        elements = saju_data.get("elements", {})
        total_elements = sum(elements.values())

        if total_elements == 0:
            return "금전운을 분석할 수 없습니다."

        dominant_element = max(elements, key=elements.get)

        money_fortunes = {
            "wood": "목(木)의 기운으로 새로운 사업이나 투자에 좋은 기회가 있을 것입니다. 교육이나 출판 관련 수입도 기대할 수 있습니다.",
            "fire": "화(火)의 기운으로 예술이나 엔터테인먼트 분야에서 수입이 증가할 수 있습니다. 창의적인 아이디어로 부수입을 얻을 기회가 있습니다.",
            "earth": "토(土)의 기운으로 부동산이나 건설 관련 수입이 안정적입니다. 실용적인 접근으로 재정적 안정을 유지할 수 있습니다.",
            "metal": "금(金)의 기운으로 금융이나 IT 분야에서 수입이 증가할 수 있습니다. 체계적인 재정 관리로 안정적인 수입을 기대할 수 있습니다.",
            "water": "수(水)의 기운으로 연구나 상담 분야에서 수입이 증가할 수 있습니다. 해외무역이나 온라인 비즈니스도 유리합니다.",
        }

        return money_fortunes.get(
            dominant_element, "올해는 안정적인 재정 관리가 중요한 한 해가 될 것입니다."
        )

    def _get_fallback_love_fortune(self, saju_data: Dict[str, Any]) -> str:
        """
        애정운 생성 실패 시 기본 애정운을 제공합니다.
        """
        elements = saju_data.get("elements", {})
        gender = saju_data.get("birth_info", {}).get("gender", "")
        total_elements = sum(elements.values())

        if total_elements == 0:
            return "애정운을 분석할 수 없습니다."

        dominant_element = max(elements, key=elements.get)

        love_fortunes = {
            "wood": "목(木)의 기운으로 새로운 만남이나 관계의 성장이 기대됩니다. 상대방과 함께 성장하는 관계를 만들어가세요.",
            "fire": "화(火)의 기운으로 열정적이고 활기찬 만남이 있을 것입니다. 예술이나 문화 활동을 통해 좋은 인연을 만날 수 있습니다.",
            "earth": "토(土)의 기운으로 안정적이고 신뢰할 수 있는 관계가 발전할 것입니다. 서로를 믿고 의지하는 관계를 만들어가세요.",
            "metal": "금(金)의 기운으로 정직하고 원칙적인 만남이 있을 것입니다. 상대방과의 소통을 통해 깊이 있는 관계를 형성할 수 있습니다.",
            "water": "수(水)의 기운으로 지혜롭고 유연한 관계가 발전할 것입니다. 상대방의 마음을 이해하고 배려하는 관계를 만들어가세요.",
        }

        base_fortune = love_fortunes.get(
            dominant_element, "올해는 진정한 사랑을 찾는 중요한 한 해가 될 것입니다."
        )

        if gender == "male":
            return f"{base_fortune} 특히 남성으로서 적극적인 마음가짐으로 좋은 인연을 만나시기 바랍니다."
        elif gender == "female":
            return f"{base_fortune} 특히 여성으로서 자신의 매력을 믿고 진정한 사랑을 찾으시기 바랍니다."
        else:
            return base_fortune


# 전역 인스턴스 생성
saju_ai = SajuAI()
