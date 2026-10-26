
# from typing import Optional

# import requests
# import streamlit as st

# # =============================
# # CONFIG
# # =============================
# # Tried in order: local first, then the hosted backend as fallback
# API_BASES = [ "https://movie-recommendation-2-1nmn.onrender.com"
#  or     "http://127.0.0.1:8000",
#     "https://movie-rec-466x.onrender.com",
# ]
# TMDB_IMG = "https://image.tmdb.org/t/p/w500"

# CATEGORIES = {
#     "trending": "Trending",
#     "popular": "Popular",
#     "top_rated": "Top Rated",
#     "now_playing": "Now Playing",
#     "upcoming": "Upcoming",
# }

# st.set_page_config(
#     page_title="CineMatch · Movie Recommender",
#     page_icon="🎬",
#     layout="wide",
#     initial_sidebar_state="collapsed",
# )

# # =============================
# # STYLES (premium dark theme + top header)
# # =============================
# st.markdown(
#     """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

# :root {
#   --bg: #0b0d12;
#   --surface: #12151c;
#   --surface-2: #181c26;
#   --border: rgba(255,255,255,0.08);
#   --text: #e8eaf0;
#   --muted: #8b92a5;
#   --accent: #e50914;
#   --accent-2: #ff6a3d;
# }

# html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
# .stApp {
#   background: radial-gradient(1200px 600px at 80% -10%, rgba(229,9,20,0.10), transparent 60%), var(--bg);
#   color: var(--text);
# }

# /* Hide default chrome + sidebar */
# [data-testid="stSidebar"], [data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"],
# #MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }

# .block-container { padding-top: 0 !important; padding-bottom: 3rem; max-width: 1400px; }

# /* ---------- Sticky top header (the columns row that contains .brand) ---------- */
# div[data-testid="stHorizontalBlock"]:has(.brand) {
#   position: sticky; top: 0; z-index: 999;
#   align-items: center !important;
#   background: rgba(11,13,18,0.88);
#   backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px);
#   border-bottom: 1px solid var(--border);
#   padding: 12px 10px; margin: 0 -10px 1.2rem -10px;
# }
# .brand { font-size: 1.35rem; font-weight: 800; letter-spacing: -0.02em; white-space: nowrap; }
# .brand span {
#   background: linear-gradient(90deg, var(--accent), var(--accent-2));
#   -webkit-background-clip: text; background-clip: text; color: transparent;
# }

# /* Category pills (radio) inside header */
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] { gap: 6px; flex-wrap: nowrap; }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label {
#   background: transparent; border: 1px solid transparent; border-radius: 999px;
#   padding: 6px 14px; margin: 0; cursor: pointer; transition: all .15s ease;
# }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:hover { background: var(--surface-2); }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label > div:first-child { display: none; }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label p {
#   font-size: 0.9rem; font-weight: 500; color: var(--muted); margin: 0;
# }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:has(input:checked) {
#   background: rgba(229,9,20,0.15); border-color: rgba(229,9,20,0.5);
# }
# div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:has(input:checked) p {
#   color: #fff; font-weight: 600;
# }

# /* Buttons */
# .stButton > button {
#   background: var(--surface-2); color: var(--text); border: 1px solid var(--border);
#   border-radius: 10px; font-weight: 600; font-size: 0.85rem; padding: 0.35rem 0.9rem; transition: all .15s ease;
# }
# .stButton > button:hover { border-color: var(--accent); color: #fff; background: rgba(229,9,20,0.18); }
# .stButton > button:focus { box-shadow: none; outline: none; }

# /* Inputs */
# .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
#   background: var(--surface) !important; border: 1px solid var(--border) !important;
#   border-radius: 12px !important; color: var(--text) !important;
# }
# .stTextInput input { padding: 0.75rem 1rem; font-size: 1rem; }
# .stTextInput input:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(229,9,20,0.18) !important; }
# .stTextInput label p, .stSelectbox label p {
#   color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: .06em; font-weight: 600;
# }

# /* Headings */
# h1, h2, h3, h4 { letter-spacing: -0.02em; color: #fff; }
# .section-title { font-size: 1.35rem; font-weight: 700; margin: 1.6rem 0 0.9rem 0; display: flex; align-items: center; gap: 10px; }
# .section-title::before { content: ""; width: 4px; height: 1.2em; border-radius: 4px; background: linear-gradient(var(--accent), var(--accent-2)); }
# .small-muted { color: var(--muted); font-size: 0.92rem; }
# hr { border-color: var(--border) !important; }

# /* Hero */
# .hero { padding: 1.2rem 0 0.4rem 0; }
# .hero h1 { font-size: 2.4rem; font-weight: 800; margin: 0 0 .3rem 0; }
# .hero p { color: var(--muted); margin: 0; font-size: 1.02rem; }

# /* Poster cards */
# .stImage img { border-radius: 14px; border: 1px solid var(--border); transition: transform .25s ease, box-shadow .25s ease; }
# .stImage img:hover { transform: translateY(-4px) scale(1.02); box-shadow: 0 14px 30px rgba(0,0,0,0.55); }
# .movie-title {
#   font-size: 0.88rem; font-weight: 600; line-height: 1.2rem; height: 2.4rem; overflow: hidden;
#   color: var(--text); margin: 6px 0 4px 0;
# }
# .no-poster {
#   aspect-ratio: 2/3; display:flex; align-items:center; justify-content:center; color: var(--muted);
#   background: var(--surface); border: 1px dashed var(--border); border-radius: 14px; font-size: .85rem;
# }

# /* Detail cards */
# .card { background: var(--surface); border: 1px solid var(--border); border-radius: 18px; padding: 22px 24px; }
# .chip {
#   display:inline-block; padding: 4px 12px; margin: 0 6px 6px 0; border-radius: 999px; font-size: .78rem;
#   font-weight: 600; background: rgba(229,9,20,0.14); border: 1px solid rgba(229,9,20,0.35); color: #ffd6d8;
# }
# .meta { color: var(--muted); font-size: .92rem; margin-bottom: 10px; }
# .overview { color: #cfd3de; line-height: 1.7; font-size: 1rem; }
# </style>
# """,
#     unsafe_allow_html=True,
# )

# # =============================
# # STATE + ROUTING (single-file pages)
# # =============================
# if "view" not in st.session_state:
#     st.session_state.view = "home"  # home | details
# if "selected_tmdb_id" not in st.session_state:
#     st.session_state.selected_tmdb_id = None

# qp_view = st.query_params.get("view")
# qp_id = st.query_params.get("id")
# if qp_view in ("home", "details"):
#     st.session_state.view = qp_view
# if qp_id:
#     try:
#         st.session_state.selected_tmdb_id = int(qp_id)
#         st.session_state.view = "details"
#     except Exception:
#         pass


# def goto_home():
#     st.session_state.view = "home"
#     st.query_params["view"] = "home"
#     if "id" in st.query_params:
#         del st.query_params["id"]
#     st.rerun()


# def goto_details(tmdb_id: int):
#     st.session_state.view = "details"
#     st.session_state.selected_tmdb_id = int(tmdb_id)
#     st.query_params["view"] = "details"
#     st.query_params["id"] = str(int(tmdb_id))
#     st.rerun()


# # =============================
# # API HELPERS
# # =============================
# @st.cache_data(ttl=60, show_spinner=False)
# def _fetch(base: str, path: str, params_items: tuple):
#     """Cached only on success: exceptions are never cached by Streamlit."""
#     r = requests.get(f"{base}{path}", params=dict(params_items), timeout=25)
#     if r.status_code >= 400:
#         raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
#     return r.json()


# def api_get_json(path: str, params: Optional[dict] = None):
#     items = tuple(sorted((params or {}).items()))
#     last_err = "Unknown error"
#     for base in API_BASES:
#         try:
#             return _fetch(base, path, items), None
#         except Exception as e:
#             last_err = f"{base} -> {e}"
#     return None, last_err


# def show_image(url):
#     """Works on both old and new Streamlit versions."""
#     try:
#         st.image(url, use_container_width=True)
#     except TypeError:
#         st.image(url, use_column_width=True)


# def poster_grid(cards, cols=6, key_prefix="grid"):
#     if not cards:
#         st.info("No movies to show.")
#         return

#     rows = (len(cards) + cols - 1) // cols
#     idx = 0
#     for r in range(rows):
#         colset = st.columns(cols)
#         for c in range(cols):
#             if idx >= len(cards):
#                 break
#             m = cards[idx]
#             idx += 1

#             tmdb_id = m.get("tmdb_id")
#             title = m.get("title", "Untitled")
#             poster = m.get("poster_url")

#             with colset[c]:
#                 if poster:
#                     show_image(poster)
#                 else:
#                     st.markdown("<div class='no-poster'>No poster</div>", unsafe_allow_html=True)

#                 st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)

#                 if st.button("View details", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
#                     if tmdb_id:
#                         goto_details(tmdb_id)


# def to_cards_from_tfidf_items(tfidf_items):
#     cards = []
#     for x in tfidf_items or []:
#         tmdb = x.get("tmdb") or {}
#         if tmdb.get("tmdb_id"):
#             cards.append(
#                 {
#                     "tmdb_id": tmdb["tmdb_id"],
#                     "title": tmdb.get("title") or x.get("title") or "Untitled",
#                     "poster_url": tmdb.get("poster_url"),
#                 }
#             )
#     return cards


# # =============================
# # Robust TMDB search parsing
# # Supports BOTH API shapes:
# # 1) raw TMDB: {"results":[{id,title,poster_path,...}]}
# # 2) list cards: [{tmdb_id,title,poster_url,...}]
# # =============================
# def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
#     keyword_l = keyword.strip().lower()

#     if isinstance(data, dict) and "results" in data:
#         raw = data.get("results") or []
#         raw_items = []
#         for m in raw:
#             title = (m.get("title") or "").strip()
#             tmdb_id = m.get("id")
#             poster_path = m.get("poster_path")
#             if not title or not tmdb_id:
#                 continue
#             raw_items.append(
#                 {
#                     "tmdb_id": int(tmdb_id),
#                     "title": title,
#                     "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
#                     "release_date": m.get("release_date", ""),
#                 }
#             )
#     elif isinstance(data, list):
#         raw_items = []
#         for m in data:
#             tmdb_id = m.get("tmdb_id") or m.get("id")
#             title = (m.get("title") or "").strip()
#             poster_url = m.get("poster_url")
#             if not title or not tmdb_id:
#                 continue
#             raw_items.append(
#                 {
#                     "tmdb_id": int(tmdb_id),
#                     "title": title,
#                     "poster_url": poster_url,
#                     "release_date": m.get("release_date", ""),
#                 }
#             )
#     else:
#         return [], []

#     matched = [x for x in raw_items if keyword_l in x["title"].lower()]
#     final_list = matched if matched else raw_items

#     suggestions = []
#     for x in final_list[:10]:
#         year = (x.get("release_date") or "")[:4]
#         label = f"{x['title']} ({year})" if year else x["title"]
#         suggestions.append((label, x["tmdb_id"]))

#     cards = [
#         {"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]}
#         for x in final_list[:limit]
#     ]
#     return suggestions, cards


# # =============================
# # TOP HEADER (replaces sidebar)
# # =============================
# h_brand, h_home, h_nav, h_cols = st.columns([1.6, 1, 6, 1.2])

# with h_brand:
#     st.markdown("<div class='brand'>🎬 <span>CineMatch</span></div>", unsafe_allow_html=True)

# with h_home:
#     if st.button("🏠 Home", key="nav_home"):
#         goto_home()

# with h_nav:
#     home_category = st.radio(
#         "Category",
#         list(CATEGORIES.keys()),
#         format_func=lambda k: CATEGORIES[k],
#         horizontal=True,
#         label_visibility="collapsed",
#         key="home_category",
#     )

# with h_cols:
#     grid_cols = st.selectbox(
#         "Columns",
#         [4, 5, 6, 7, 8],
#         index=2,
#         label_visibility="collapsed",
#         key="grid_cols",
#         help="Grid columns",
#     )

# # ==========================================================
# # VIEW: HOME
# # ==========================================================
# if st.session_state.view == "home":
#     st.markdown(
#         """
# <div class='hero'>
#   <h1>Find your next favourite movie</h1>
#   <p>Search any title, open it, and get smart recommendations based on story and genre.</p>
# </div>
# """,
#         unsafe_allow_html=True,
#     )

#     typed = st.text_input(
#         "Search by movie title",
#         placeholder="Try: avengers, batman, love…",
#     )

#     # SEARCH MODE
#     if typed.strip():
#         if len(typed.strip()) < 2:
#             st.caption("Type at least 2 characters for suggestions.")
#         else:
#             data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

#             if err or data is None:
#                 st.error(f"Search failed: {err}")
#             else:
#                 suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

#                 if suggestions:
#                     labels = ["-- Select a movie --"] + [s[0] for s in suggestions]
#                     selected = st.selectbox("Suggestions", labels, index=0)

#                     if selected != "-- Select a movie --":
#                         label_to_id = {s[0]: s[1] for s in suggestions}
#                         goto_details(label_to_id[selected])
#                 else:
#                     st.info("No suggestions found. Try another keyword.")

#                 st.markdown("<div class='section-title'>Search results</div>", unsafe_allow_html=True)
#                 poster_grid(cards, cols=grid_cols, key_prefix="search_results")

#         st.stop()

#     # HOME FEED MODE
#     st.markdown(
#         f"<div class='section-title'>{CATEGORIES[home_category]}</div>",
#         unsafe_allow_html=True,
#     )

#     home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 24})
#     if err or not home_cards:
#         st.error(
#             "Couldn't load the home feed. The backend may be waking up or "
#             "TMDB may be unreachable on your network."
#         )
#         st.caption(f"Details: {err or 'Unknown error'}")
#         if st.button("🔄 Retry", key="retry_home"):
#             st.rerun()
#         st.stop()

#     poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

# # ==========================================================
# # VIEW: DETAILS
# # ==========================================================
# elif st.session_state.view == "details":
#     tmdb_id = st.session_state.selected_tmdb_id
#     if not tmdb_id:
#         st.warning("No movie selected.")
#         if st.button("← Back to Home"):
#             goto_home()
#         st.stop()

#     if st.button("← Back to Home", key="back_top"):
#         goto_home()

#     data, err = api_get_json(f"/movie/id/{tmdb_id}")
#     if err or not data:
#         st.error(f"Could not load details: {err or 'Unknown error'}")
#         st.stop()

#     # Backdrop banner
#     if data.get("backdrop_url"):
#         show_image(data["backdrop_url"])

#     left, right = st.columns([1, 2.4], gap="large")

#     with left:
#         if data.get("poster_url"):
#             show_image(data["poster_url"])
#         else:
#             st.markdown("<div class='no-poster'>No poster</div>", unsafe_allow_html=True)

#     with right:
#         release = data.get("release_date") or "-"
#         genre_names = [g["name"] for g in data.get("genres", [])]
#         chips = "".join(f"<span class='chip'>{g}</span>" for g in genre_names) or "<span class='small-muted'>-</span>"
#         overview = data.get("overview") or "No overview available."

#         st.markdown(
#             f"""
# <div class='card'>
#   <h1 style='margin:0 0 6px 0;'>{data.get('title','')}</h1>
#   <div class='meta'>📅 Release: {release}</div>
#   <div style='margin-bottom:14px;'>{chips}</div>
#   <h4 style='margin:10px 0 6px 0;'>Overview</h4>
#   <div class='overview'>{overview}</div>
# </div>
# """,
#             unsafe_allow_html=True,
#         )

#     st.markdown("<div class='section-title'>Recommended for you</div>", unsafe_allow_html=True)

#     title = (data.get("title") or "").strip()
#     if title:
#         bundle, err2 = api_get_json(
#             "/movie/search",
#             params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
#         )

#         if not err2 and bundle:
#             st.markdown("#### 🔎 Similar movies")
#             poster_grid(
#                 to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")),
#                 cols=grid_cols,
#                 key_prefix="details_tfidf",
#             )

#             st.markdown("#### 🎭 More like this (genre)")
#             poster_grid(
#                 bundle.get("genre_recommendations", []),
#                 cols=grid_cols,
#                 key_prefix="details_genre",
#             )
#         else:
#             st.info("Showing genre recommendations (fallback).")
#             genre_only, err3 = api_get_json(
#                 "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
#             )
#             if not err3 and genre_only:
#                 poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
#             else:
#                 st.warning("No recommendations available right now.")
#     else:
#         st.warning("No title available to compute recommendations.")




import time
from typing import Optional

import requests
import streamlit as st

# =============================
# CONFIG
# =============================
# Tried in order: local first, then the hosted backend as fallback
API_BASES = [ 
    "https://movie-recommendation-2-1nmn.onrender.com",
    "http://127.0.0.1:8000",
    "https://movie-rec-466x.onrender.com",
]
TMDB_IMG = "https://image.tmdb.org/t/p/w500"
TMDB_BACKDROP = "https://image.tmdb.org/t/p/original"

CATEGORIES = {
    "trending": "Trending",
    "popular": "Popular",
    "top_rated": "Top Rated",
    "now_playing": "Now Playing",
    "upcoming": "Upcoming",
}

st.set_page_config(
    page_title="CineMatch · Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =============================
# STYLES (Responsive Premium Dark)
# =============================
st.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
  --bg: #0b0d12;
  --surface: #12151c;
  --surface-2: #181c26;
  --border: rgba(255,255,255,0.08);
  --text: #e8eaf0;
  --muted: #8b92a5;
  --accent: #e50914;
  --accent-2: #ff6a3d;
}

html, body, [class*="css"], .stApp { font-family: 'Inter', sans-serif; }
.stApp {
  background: radial-gradient(1200px 600px at 80% -10%, rgba(229,9,20,0.08), transparent 60%), var(--bg);
  color: var(--text);
}

/* Hide default chrome + sidebar */
[data-testid="stSidebar"], [data-testid="collapsedControl"], [data-testid="stSidebarCollapsedControl"],
#MainMenu, footer, header[data-testid="stHeader"] { display: none !important; }

.block-container { padding-top: 0 !important; padding-bottom: 4rem; max-width: 1400px; }

/* ---------- Sticky Top Header ---------- */
div[data-testid="stHorizontalBlock"]:has(.brand) {
  position: sticky; top: 0; z-index: 999;
  align-items: center !important;
  background: rgba(11,13,18,0.92);
  backdrop-filter: blur(16px); -webkit-backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 12px 16px; margin: 0 -1rem 2rem -1rem;
  display: flex !important; flex-wrap: nowrap !important; gap: 1rem;
}
.brand { font-size: 1.4rem; font-weight: 800; letter-spacing: -0.02em; white-space: nowrap; }
.brand span {
  background: linear-gradient(90deg, var(--accent), var(--accent-2));
  -webkit-background-clip: text; background-clip: text; color: transparent;
}

/* Header Category Pills */
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] { gap: 8px; flex-wrap: nowrap; overflow-x: auto; }
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"]::-webkit-scrollbar { display: none; }
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label {
  background: transparent; border: 1px solid transparent; border-radius: 999px;
  padding: 6px 16px; margin: 0; cursor: pointer; transition: all .2s ease;
}
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:hover { background: var(--surface-2); }
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label > div:first-child { display: none; }
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label p {
  font-size: 0.9rem; font-weight: 500; color: var(--muted); margin: 0; white-space: nowrap;
}
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:has(input:checked) {
  background: rgba(229,9,20,0.15); border-color: rgba(229,9,20,0.5);
}
div[data-testid="stHorizontalBlock"]:has(.brand) div[role="radiogroup"] label:has(input:checked) p {
  color: #fff; font-weight: 600;
}

/* Streamlit Native Buttons */
.stButton > button {
  background: var(--surface-2); color: var(--text); border: 1px solid var(--border);
  border-radius: 10px; font-weight: 600; font-size: 0.85rem; padding: 0.4rem 1rem; width: 100%; transition: all .2s ease;
}
.stButton > button:hover { border-color: var(--accent); color: #fff; background: rgba(229,9,20,0.18); transform: translateY(-1px); }
.stButton > button:focus { box-shadow: 0 0 0 3px rgba(229,9,20,0.25); outline: none; border-color: var(--accent); color: #fff;}

/* Inputs */
.stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
  background: var(--surface) !important; border: 1px solid var(--border) !important;
  border-radius: 12px !important; color: var(--text) !important; box-shadow: none !important;
}
.stTextInput input { padding: 0.8rem 1.2rem; font-size: 1rem; transition: border .2s ease; }
.stTextInput input:focus { border-color: var(--accent) !important; box-shadow: 0 0 0 3px rgba(229,9,20,0.15) !important; }
.stTextInput label p, .stSelectbox label p {
  color: var(--muted); font-size: 0.8rem; text-transform: uppercase; letter-spacing: .06em; font-weight: 600;
}

/* Typography & Headings */
h1, h2, h3, h4 { letter-spacing: -0.02em; color: #fff; }
.section-title { font-size: 1.4rem; font-weight: 700; margin: 2rem 0 1.2rem 0; display: flex; align-items: center; gap: 12px; }
.section-title::before { content: ""; width: 5px; height: 1.2em; border-radius: 4px; background: linear-gradient(180deg, var(--accent), var(--accent-2)); }
.small-muted { color: var(--muted); font-size: 0.92rem; }
hr { border-color: var(--border) !important; margin: 2.5rem 0; }

/* Hero Section */
.hero { padding: 2rem 0 1.5rem 0; text-align: center; }
.hero h1 { font-size: 2.8rem; font-weight: 800; margin: 0 0 .5rem 0; text-shadow: 0 4px 20px rgba(0,0,0,0.4); }
.hero p { color: var(--muted); margin: 0 auto; font-size: 1.1rem; max-width: 600px; line-height: 1.5; }

/* Cinematic Backdrop Banner */
.cinematic-banner {
    width: 100%; height: 350px;
    background-size: cover; background-position: center;
    border-radius: 20px; margin-bottom: 2rem;
    position: relative; overflow: hidden;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6);
}
.cinematic-banner::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(0deg, var(--bg) 0%, rgba(11,13,18,0.2) 60%, rgba(11,13,18,0.8) 100%);
}

/* Poster Cards */
.stImage img { border-radius: 12px; border: 1px solid var(--border); transition: transform .3s ease, box-shadow .3s ease; object-fit: cover; }
.stImage img:hover { transform: translateY(-6px) scale(1.03); box-shadow: 0 15px 35px rgba(0,0,0,0.6); z-index: 10; }
.movie-title {
  font-size: 0.9rem; font-weight: 600; line-height: 1.3rem; height: 2.6rem; overflow: hidden;
  color: var(--text); margin: 10px 0 6px 0; text-align: center;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; text-overflow: ellipsis;
}
.no-poster {
  aspect-ratio: 2/3; display:flex; align-items:center; justify-content:center; color: var(--muted);
  background: var(--surface-2); border: 1px dashed var(--border); border-radius: 12px; font-size: .85rem; text-transform: uppercase; letter-spacing: 1px;
}

/* Detail Cards */
.card { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.2); }
.chip {
  display:inline-block; padding: 6px 14px; margin: 0 8px 8px 0; border-radius: 999px; font-size: .8rem;
  font-weight: 600; background: rgba(229,9,20,0.1); border: 1px solid rgba(229,9,20,0.3); color: #ffd6d8;
  backdrop-filter: blur(4px);
}
.meta { color: var(--accent-2); font-size: .95rem; font-weight: 600; margin-bottom: 16px; display: flex; gap: 15px; }
.overview { color: #cfd3de; line-height: 1.8; font-size: 1.05rem; margin-top: 15px; }

/* Responsive Adjustments */
@media (max-width: 768px) {
  .hero h1 { font-size: 2rem; }
  .brand { font-size: 1.1rem; }
  div[data-testid="stHorizontalBlock"]:has(.brand) { flex-wrap: wrap !important; justify-content: space-between; padding: 10px; margin-bottom: 1rem; }
  .cinematic-banner { height: 200px; border-radius: 12px; }
  .card { padding: 20px; }
  .block-container { padding-bottom: 2rem; }
}
</style>
""",
    unsafe_allow_html=True,
)

# =============================
# STATE + ROUTING
# =============================
if "view" not in st.session_state:
    st.session_state.view = "home"
if "selected_tmdb_id" not in st.session_state:
    st.session_state.selected_tmdb_id = None

qp_view = st.query_params.get("view")
qp_id = st.query_params.get("id")
if qp_view in ("home", "details"):
    st.session_state.view = qp_view
if qp_id:
    try:
        st.session_state.selected_tmdb_id = int(qp_id)
        st.session_state.view = "details"
    except Exception:
        pass

def goto_home():
    st.session_state.view = "home"
    st.query_params["view"] = "home"
    if "id" in st.query_params:
        del st.query_params["id"]
    st.rerun()

def goto_details(tmdb_id: int):
    st.session_state.view = "details"
    st.session_state.selected_tmdb_id = int(tmdb_id)
    st.query_params["view"] = "details"
    st.query_params["id"] = str(int(tmdb_id))
    st.rerun()

# =============================
# API HELPERS
# =============================
@st.cache_data(ttl=60, show_spinner=False)
def _fetch(base: str, path: str, params_items: tuple):
    r = requests.get(f"{base}{path}", params=dict(params_items), timeout=25)
    if r.status_code >= 400:
        raise RuntimeError(f"HTTP {r.status_code}: {r.text[:200]}")
    return r.json()

def api_get_json(path: str, params: Optional[dict] = None):
    items = tuple(sorted((params or {}).items()))
    last_err = "Unknown error"
    for base in API_BASES:
        try:
            return _fetch(base, path, items), None
        except Exception as e:
            last_err = f"{base} -> {e}"
    return None, last_err

def show_image(url):
    """Works on both old and new Streamlit versions."""
    try:
        st.image(url, use_container_width=True)
    except TypeError:
        st.image(url, use_column_width=True)

def poster_grid(cards, cols=6, key_prefix="grid"):
    if not cards:
        st.info("No movies to show here right now.", icon="🍿")
        return

    rows = (len(cards) + cols - 1) // cols
    idx = 0
    
    # Streamlit handles columns automatically responding to screen width natively
    for r in range(rows):
        colset = st.columns(cols)
        for c in range(cols):
            if idx >= len(cards):
                break
            m = cards[idx]
            idx += 1

            tmdb_id = m.get("tmdb_id")
            title = m.get("title", "Untitled")
            poster = m.get("poster_url")

            with colset[c]:
                # Poster Image
                if poster:
                    show_image(poster)
                else:
                    st.markdown("<div class='no-poster'>No Poster</div>", unsafe_allow_html=True)
                
                # Title & Button Container
                st.markdown(f"<div class='movie-title'>{title}</div>", unsafe_allow_html=True)
                if st.button("Details", key=f"{key_prefix}_{r}_{c}_{idx}_{tmdb_id}"):
                    if tmdb_id:
                        goto_details(tmdb_id)

def to_cards_from_tfidf_items(tfidf_items):
    cards = []
    for x in tfidf_items or []:
        tmdb = x.get("tmdb") or {}
        if tmdb.get("tmdb_id"):
            cards.append({
                "tmdb_id": tmdb["tmdb_id"],
                "title": tmdb.get("title") or x.get("title") or "Untitled",
                "poster_url": tmdb.get("poster_url"),
            })
    return cards

def parse_tmdb_search_to_cards(data, keyword: str, limit: int = 24):
    keyword_l = keyword.strip().lower()
    raw_items = []

    if isinstance(data, dict) and "results" in data:
        for m in (data.get("results") or []):
            title = (m.get("title") or "").strip()
            tmdb_id = m.get("id")
            poster_path = m.get("poster_path")
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": f"{TMDB_IMG}{poster_path}" if poster_path else None,
                    "release_date": m.get("release_date", ""),
                })
    elif isinstance(data, list):
        for m in data:
            tmdb_id = m.get("tmdb_id") or m.get("id")
            title = (m.get("title") or "").strip()
            if title and tmdb_id:
                raw_items.append({
                    "tmdb_id": int(tmdb_id),
                    "title": title,
                    "poster_url": m.get("poster_url"),
                    "release_date": m.get("release_date", ""),
                })
    
    if not raw_items:
        return [], []

    matched = [x for x in raw_items if keyword_l in x["title"].lower()]
    final_list = matched if matched else raw_items

    suggestions = []
    for x in final_list[:10]:
        year = (x.get("release_date") or "")[:4]
        label = f"{x['title']} ({year})" if year else x["title"]
        suggestions.append((label, x["tmdb_id"]))

    cards = [{"tmdb_id": x["tmdb_id"], "title": x["title"], "poster_url": x["poster_url"]} for x in final_list[:limit]]
    return suggestions, cards


# =============================
# TOP HEADER 
# =============================
# Streamlit columns are used, but CSS enforces flexbox row for navigation stability on mobile
h_brand, h_home, h_nav, h_cols = st.columns([1.5, 1, 6, 1.5])

with h_brand:
    st.markdown("<div class='brand'>🎬 <span>CineMatch</span></div>", unsafe_allow_html=True)

with h_home:
    if st.button("🏠 Home", key="nav_home"):
        goto_home()

with h_nav:
    home_category = st.radio(
        "Category",
        list(CATEGORIES.keys()),
        format_func=lambda k: CATEGORIES[k],
        horizontal=True,
        label_visibility="collapsed",
        key="home_category",
    )

with h_cols:
    grid_cols = st.selectbox(
        "Columns",
        [4, 5, 6, 7, 8],
        index=2,
        label_visibility="collapsed",
        key="grid_cols",
        help="Adjust the number of columns in the grid",
    )

# ==========================================================
# VIEW: HOME
# ==========================================================
if st.session_state.view == "home":
    st.markdown(
        """
        <div class='hero'>
          <h1>Find your next favourite movie.</h1>
          <p>Search any title, open it, and get smart recommendations based on story and genre profiling.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    typed = st.text_input(
        "Search by movie title",
        placeholder="Try: Inception, The Matrix, Interstellar...",
    )

    # SEARCH MODE
    if typed.strip():
        if len(typed.strip()) < 2:
            st.caption("Type at least 2 characters for suggestions.")
        else:
            with st.spinner("Searching..."):
                data, err = api_get_json("/tmdb/search", params={"query": typed.strip()})

            if err or data is None:
                st.error(f"Search failed: {err}")
            else:
                suggestions, cards = parse_tmdb_search_to_cards(data, typed.strip(), limit=24)

                if suggestions:
                    labels = ["-- Select a movie directly --"] + [s[0] for s in suggestions]
                    selected = st.selectbox("Quick Suggestions", labels, index=0)

                    if selected != "-- Select a movie directly --":
                        label_to_id = {s[0]: s[1] for s in suggestions}
                        goto_details(label_to_id[selected])
                else:
                    st.info("No suggestions found. Try another keyword.")

                st.markdown("<div class='section-title'>Search Results</div>", unsafe_allow_html=True)
                poster_grid(cards, cols=grid_cols, key_prefix="search_results")

        st.stop()

    # HOME FEED MODE
    st.markdown(f"<div class='section-title'>{CATEGORIES[home_category]} Movies</div>", unsafe_allow_html=True)

    with st.spinner("Loading feed..."):
        home_cards, err = api_get_json("/home", params={"category": home_category, "limit": 24})
        
    if err or not home_cards:
        st.error(
            "Couldn't load the home feed. The backend may be waking up or "
            "TMDB may be unreachable on your network."
        )
        st.caption(f"Details: {err or 'Unknown error'}")
        if st.button("🔄 Retry Connection", key="retry_home"):
            st.rerun()
        st.stop()

    poster_grid(home_cards, cols=grid_cols, key_prefix="home_feed")

# ==========================================================
# VIEW: DETAILS
# ==========================================================
elif st.session_state.view == "details":
    tmdb_id = st.session_state.selected_tmdb_id
    if not tmdb_id:
        st.warning("No movie selected.")
        if st.button("← Back to Home"):
            goto_home()
        st.stop()

    with st.spinner("Fetching movie details and smart recommendations..."):
        data, err = api_get_json(f"/movie/id/{tmdb_id}")
        
    if err or not data:
        st.error(f"Could not load details: {err or 'Unknown error'}")
        if st.button("← Back to Home", key="err_back"):
            goto_home()
        st.stop()

    # Cinematic Backdrop Banner
    backdrop = data.get("backdrop_url")
    if backdrop:
        # Swap w500 to original for higher resolution backdrops if it contains standard tmdb img path
        backdrop = backdrop.replace("/w500/", "/original/") 
        st.markdown(
            f"<div class='cinematic-banner' style='background-image: url(\"{backdrop}\");'></div>", 
            unsafe_allow_html=True
        )

    # Main details layout
    left, right = st.columns([1, 2.5], gap="large")

    with left:
        if data.get("poster_url"):
            show_image(data["poster_url"])
        else:
            st.markdown("<div class='no-poster' style='height: 400px;'>No poster</div>", unsafe_allow_html=True)
            
        if st.button("← Back to Home", key="back_sidebar"):
            goto_home()

    with right:
        release = data.get("release_date") or "Unknown Date"
        genre_names = [g["name"] for g in data.get("genres", [])]
        chips = "".join(f"<span class='chip'>{g}</span>" for g in genre_names) or "<span class='small-muted'>-</span>"
        overview = data.get("overview") or "No overview available for this title."
        rating = data.get("vote_average", 0.0)
        rating_ui = f"⭐️ {round(rating, 1)} / 10" if rating else "No rating"

        st.markdown(
            f"""
            <div class='card'>
              <h1 style='margin:0 0 10px 0; font-size: 2.2rem;'>{data.get('title','')}</h1>
              <div class='meta'>
                 <span>📅 {release}</span>
                 <span>{rating_ui}</span>
              </div>
              <div style='margin-bottom:20px;'>{chips}</div>
              <h4 style='margin:10px 0 8px 0; font-size: 1.1rem; color: #fff;'>Overview</h4>
              <div class='overview'>{overview}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>Recommended For You</div>", unsafe_allow_html=True)

    title = (data.get("title") or "").strip()
    if title:
        with st.spinner("Generating AI-driven recommendations..."):
            bundle, err2 = api_get_json(
                "/movie/search",
                params={"query": title, "tfidf_top_n": 12, "genre_limit": 12},
            )

        if not err2 and bundle:
            st.markdown("#### 🧠 Story-Based Matches (AI)", help="Movies with similar plot lines based on TF-IDF analysis.")
            poster_grid(
                to_cards_from_tfidf_items(bundle.get("tfidf_recommendations")),
                cols=grid_cols,
                key_prefix="details_tfidf",
            )

            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown("#### 🎭 More in this Genre", help="Top rated movies sharing similar genres.")
            poster_grid(
                bundle.get("genre_recommendations", []),
                cols=grid_cols,
                key_prefix="details_genre",
            )
        else:
            st.info("Showing genre recommendations (fallback).", icon="ℹ️")
            genre_only, err3 = api_get_json(
                "/recommend/genre", params={"tmdb_id": tmdb_id, "limit": 18}
            )
            if not err3 and genre_only:
                poster_grid(genre_only, cols=grid_cols, key_prefix="details_genre_fallback")
            else:
                st.warning("No recommendations available right now.")
    else:
        st.warning("No title available to compute recommendations.")