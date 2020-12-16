import streamlit as st
from pathlib import Path
from streamlit_discourse import st_discourse

"""
# 💬 Streamlit Discourse [![GitHub][github_badge]][github_link] [![PyPI][pypi_badge]][pypi_link]

[github_badge]: https://badgen.net/badge/icon/GitHub?icon=github&color=black&label
[github_link]: https://github.com/okld/streamlit-discourse

[pypi_badge]: https://badgen.net/pypi/v/streamlit-discourse?icon=pypi&color=black&label
[pypi_link]: https://pypi.org/project/streamlit-discourse

---

This demo application showcases Streamlit Discourse component. If you want your comment to be displayed below, please feel free to reply to this topic: [Discourse component](https://discuss.streamlit.io/t/discourse-component/8061)

"""

with st.beta_expander("Component docstring"):
    st_discourse

with st.beta_expander("Demo source code"):
    st.code(Path(__file__).read_text())

"---"

st_discourse("discuss.streamlit.io", 8061, key="discourse")
