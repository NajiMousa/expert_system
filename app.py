# import streamlit as st
# import matplotlib.pyplot as plt # type: ignore
# import numpy as np
# import pandas as pd

# # تحميل البيانات مع تحديد الترميز
# summer_data = pd.read_csv('data/transformer_data_summer.csv', encoding='utf-8')

# # عرض أول 5 صفوف للتأكد من البيانات
# print(summer_data.head())

# rules = [
#     {"condition": lambda R, S, T: R > 100 or S > 100 or T > 100, "action": "تحذير: تيار مرتفع على الأقل في أحد الفازات"},
#     {"condition": lambda R, S, T: R <= 100 and S <= 100 and T <= 100, "action": "الوضع طبيعي: التيار ضمن الحدود الطبيعية"},
# ]
# rules += [
#     {"condition": lambda RS, RT, ST, RN, SN, TN: RS < 200 or RT < 200 or ST < 200, "action": "تحذير: انخفاض في الجهد بين الفازات"},
#     {"condition": lambda RS, RT, ST, RN, SN, TN: RS >= 200 and RT >= 200 and ST >= 200, "action": "الوضع طبيعي: الجهد بين الفازات ضمن الحد المطلوب"},
# ]
# rules += [
#     {"condition": lambda R, S, T: abs(R - S) > 50 or abs(S - T) > 50 or abs(R - T) > 50, "action": "تحذير: عدم توازن بين الفازات في التيار"},
#     {"condition": lambda R, S, T: abs(R - S) <= 50 and abs(S - T) <= 50 and abs(R - T) <= 50, "action": "الوضع طبيعي: التيار متوازن بين الفازات"},
# ]
# rules += [
#     {"condition": lambda قدرة: قدرة > 100, "action": "تحذير: قدرة السكينة عالية جداً"},
#     {"condition": lambda قدرة: قدرة <= 100, "action": "الوضع طبيعي: قدرة السكينة ضمن الحدود المسموحة"},
#     {"condition": lambda قدرة: قدرة > 80, "action": "تحذير: المحول يعمل بأقصى قدرته, استهلاك عالي"},
#     {"condition": lambda قدرة: قدرة <= 80, "action": "الوضع طبيعي: المحول يعمل بكفاءة مناسبة"},
#     {"condition": lambda اتجاه_السكينة: اتجاه_السكينة == "غير طبيعي", "action": "تحذير: اتجاه السكينة غير طبيعي"},
#     {"condition": lambda اتجاه_السكينة: اتجاه_السكينة == "طبيعي", "action": "الوضع طبيعي: اتجاه السكينة طبيعي"},
# ]
# rules += [
#     {"condition": lambda نظام_القياس: نظام_القياس == "القياس التقليدي", "action": "تحذير: النظام القياسي قد لا يكون دقيقًا"},
#     {"condition": lambda نظام_القياس: نظام_القياس == "القياس الرقمي", "action": "الوضع طبيعي: النظام القياسي دقيق"},
# ]

# rules = [
#     {"condition": lambda R, S, T: R > 100 or S > 100 or T > 100, "action": "تحذير: تيار مرتفع على الأقل في أحد الفازات"},
#     {"condition": lambda R, S, T: R <= 100 and S <= 100 and T <= 100, "action": "الوضع طبيعي: التيار ضمن الحدود الطبيعية"},
#     {"condition": lambda RS, RT, ST, RN, SN, TN: RS < 200 or RT < 200 or ST < 200, "action": "تحذير: انخفاض في الجهد بين الفازات"},
#     {"condition": lambda RS, RT, ST, RN, SN, TN: RS >= 200 and RT >= 200 and ST >= 200, "action": "الوضع طبيعي: الجهد بين الفازات ضمن الحد المطلوب"},

#     {"condition": lambda R, S, T: abs(R - S) > 50 or abs(S - T) > 50 or abs(R - T) > 50, "action": "تحذير: عدم توازن بين الفازات في التيار"},
#     {"condition": lambda R, S, T: abs(R - S) <= 50 and abs(S - T) <= 50 and abs(R - T) <= 50, "action": "الوضع طبيعي: التيار متوازن بين الفازات"},

#     {"condition": lambda قدرة: قدرة > 100, "action": "تحذير: قدرة السكينة عالية جداً"},
#     {"condition": lambda قدرة: قدرة <= 100, "action": "الوضع طبيعي: قدرة السكينة ضمن الحدود المسموحة"},

#     {"condition": lambda قدرة: قدرة > 80, "action": "تحذير: المحول يعمل بأقصى قدرته, استهلاك عالي"},
#     {"condition": lambda قدرة: قدرة <= 80, "action": "الوضع طبيعي: المحول يعمل بكفاءة مناسبة"},

#     {"condition": lambda اتجاه_السكينة: اتجاه_السكينة == "غير طبيعي", "action": "تحذير: اتجاه السكينة غير طبيعي"},
#     {"condition": lambda اتجاه_السكينة: اتجاه_السكينة == "طبيعي", "action": "الوضع طبيعي: اتجاه السكينة طبيعي"},

#     {"condition": lambda نظام_القياس: نظام_القياس == "القياس التقليدي", "action": "تحذير: النظام القياسي قد لا يكون دقيقًا"}]
# import streamlit as st
# import pandas as pd

# # بيانات المحولات
# data = pd.DataFrame({
#     "رقم المحول": ["T1", "T2"],
#     "القدرة": [85, 60]
# })

# # القواعد
# rules = [
#     {"condition": lambda القدرة: القدرة > 80, "action": "تحذير: حمل زائد"},
#     {"condition": lambda القدرة: القدرة <= 80, "action": "الوضع طبيعي"}
# ]

# # محرك الاستدلال
# def inference_engine(data, rules):
#     results = []
#     for _, row in data.iterrows():
#         for rule in rules:
#             if rule["condition"](row["القدرة"]):
#                 results.append({"رقم المحول": row["رقم المحول"], "الإجراء": rule["action"]})
#     return results

# # واجهة تفاعلية باستخدام Streamlit
# st.title("نظام خبير لتحليل بيانات المحولات")
# st.write("قم بإدخال معطيات المحول")

# # إدخال المستخدم
# رقم_المحول = st.selectbox("اختار رقم المحول", data["رقم المحول"])
# القدرة = st.number_input("أدخل قدرة المحول", min_value=0, max_value=100, value=60)

# # تطبيق القواعد على المدخلات
# input_data = pd.DataFrame({"رقم المحول": [رقم_المحول], "القدرة": [القدرة]})
# results = inference_engine(input_data, rules)

# # عرض النتائج
# if results:
#     st.write("نتائج النظام الخبير:")
#     st.write(results)
# else:
#     st.write("لا توجد نتائج مطابقة.")


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# بيانات المحولات
data = pd.DataFrame({
    "رقم المحول": ["T1", "T2", "T3"],
    "القدرة": [85, 60, 70]
})

# القواعد
rules = [
    {"condition": lambda القدرة: القدرة > 80, "action": "تحذير: حمل زائد"},
    {"condition": lambda القدرة: القدرة <= 80, "action": "الوضع طبيعي"}
]

# محرك الاستدلال
def inference_engine(data, rules):
    results = []
    for _, row in data.iterrows():
        for rule in rules:
            if rule["condition"](row["القدرة"]):
                results.append({"رقم المحول": row["رقم المحول"], "الإجراء": rule["action"]})
    return results

# واجهة تفاعلية باستخدام Streamlit
st.set_page_config(layout="wide")
st.title("نظام خبير لتحليل بيانات المحولات")

# تقسيم الشاشة إلى عمودين
col1, col2 = st.columns(2)

# القسم الأول: إدخال البيانات
with col1:
    st.header("إدخال بيانات المحول")
    رقم_المحول = st.selectbox("اختر رقم المحول", data["رقم المحول"])
    القدرة = st.number_input("أدخل قدرة المحول (kW)", min_value=0, max_value=100, value=60)

    # تحديث البيانات بناءً على المدخلات
    input_data = pd.DataFrame({"رقم المحول": [رقم_المحول], "القدرة": [القدرة]})
    results = inference_engine(input_data, rules)

# القسم الثاني: عرض النتائج
with col2:
    st.header("نتائج النظام الخبير")

    if results:
        # عرض النتائج في جدول
        st.subheader("النتائج التفصيلية")
        results_df = pd.DataFrame(results)
        st.table(results_df)

        # عرض النتائج في مخطط دائري
        st.subheader("عرض النتائج في مخطط دائري")
        action_counts = results_df["الإجراء"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(action_counts, labels=action_counts.index, autopct="%1.1f%%", startangle=90, colors=["#ff9999", "#66b3ff"])
        ax.axis('equal')  # لضمان أن الدائرة مستديرة
        st.pyplot(fig)

    else:
        st.write("لا توجد نتائج مطابقة.")

# عرض جميع بيانات المحولات في جدول مع حالة كل محول
st.header("جميع بيانات المحولات")
all_results = inference_engine(data, rules)
all_results_df = pd.DataFrame(all_results)
st.write(data.merge(all_results_df, on="رقم المحول", how="left"))
