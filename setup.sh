mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT -p\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
