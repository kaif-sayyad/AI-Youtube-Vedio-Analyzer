import streamlit as st
from analyzer import  build_youtube_agent

st.set_page_config(
    page_title="Youtube vedio analyzer",
    layout = "wide"
)

st.markdown(
    """
<style>
.main{
    background-color : #f5f7fa;
    }

.stButton>button{
    width: 100%;
    background-color: #ff4b4b;
    color : white;
    border-radius: 10px;
    height: 3em;
    font-size: 18px;
    border: none;
}


.stButton>button.hover{
    background-color: #d93636;
}

.result-box{
    padding: 20px;
    border-radius: 12px;
    background: #ffffff;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.1);
}
</style>
    """,
unsafe_allow_html=True
)
st.title("AI Youtube Vedio Analyzer")

@st.cache_resource
def get_agent():
    return build_youtube_agent()

agent = get_agent()

col1,col2 = st.columns([3,1])

with col1:
    video_url = st.text_input(
        "Youtube Video URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

with col2:
    st.write("")
    st.write("")
    analyze =st.button("Analyze")

if video_url and analyze:
    with st.spinner("Analyzing vedio...."):
        response = agent.run(
            f"Analyze this vedio: {video_url}"
        )

    st.success("Analysis Completed")
    st.markdown("<div class='result-box'>",
                unsafe_allow_html=True)
    st.subheader("Analysis Result")
    st.write(response.content)
    st.markdown("<div>", unsafe_allow_html=True)
