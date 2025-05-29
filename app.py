import streamlit as st

subject_items = {'국어': [('고쳐쓰기', 20.0), ('발표', 20.0), ('중간', 30.0), ('기말', 30.0)], '영어': [('기행문', 30.0), ('발표하기', 10.0), ('중간', 30.0), ('기말', 30.0)], '수학': [('서술형', 30.0), ('말하기', 10.0), ('중간', 30.0), ('기말', 30.0)], '과학': [('전류계산', 20.0), ('여행계획', 20.0), ('중간', 30.0), ('기말', 30.0)], '도덕': [('말하기', 30.0), ('쓰기', 30.0), ('기말', 40.0)], '역사': [('보고서', 30.0), ('백과사전', 10.0), ('중간', 30.0), ('기말', 30.0)], '기술가정': [('보고서1', 20.0), ('보고서2', 20.0), ('서술형', 30.0), ('기말', 30.0)], '컴퓨팅과 융합': [('문제해결', 20.0), ('글쓰기', 20.0), ('기말', 60.0)]}

grade_thresholds = {
    "A": 89.5,
    "B": 79.5,
    "C": 69.5,
    "D": 59.5,
    "E": 0
}

st.title("🎯 기말고사 목표 점수 계산기")
st.markdown("과목과 목표 등급을 선택하고 현재까지의 점수를 입력하세요.")

subject = st.selectbox("과목 선택", list(subject_items.keys()))
target_grade = st.selectbox("목표 등급 선택", list(grade_thresholds.keys()))

scores = []
st.markdown("#### 📥 세부 평가 점수 입력")
for label, weight in subject_items[subject]:
    if "기말" in label:
        continue  # 기말고사 항목만 제외
    score = st.number_input(f"{label} ({weight}%)", min_value=0.0, max_value=100.0, step=0.5, key=label + subject)
    scores.append((score, weight))

if st.button("🎯 기말고사 목표 점수 계산"):
    total_current = sum(score * weight / 100 for score, weight in scores)
    remaining_weight = 100 - sum(weight for _, weight in scores)

    if remaining_weight <= 0:
        st.warning("⚠️ 기말고사 반영 비율이 0%입니다. 목표 점수 계산이 불가능합니다.")
    else:
        needed_score = (grade_thresholds[target_grade] - total_current) / (remaining_weight / 100)

        if needed_score > 100:
            st.error(f"❌ {target_grade} 등급은 기말고사 100점으로도 불가능합니다.")
        elif needed_score < 0:
            st.success(f"✅ 이미 {target_grade} 등급을 넘었습니다!")
        else:
            st.info(f"📌 {target_grade} 등급을 위해 기말고사에서 **최소 {needed_score:.2f}점**이 필요합니다.")


 
