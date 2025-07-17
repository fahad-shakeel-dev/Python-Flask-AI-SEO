# from flask import Blueprint, render_template, request, jsonify
# from ..analyzer import extract_keywords, get_readability, grammar_and_spelling, summarize_text, sentiment_analysis, seo_score, lint_html, get_content_stats
# import requests
# from bs4 import BeautifulSoup
#
# dashboard = Blueprint('dashboard', __name__)
#
# @dashboard.route('/dashboard', methods=['GET', 'POST'])
# def dashboard():
#     feature = request.args.get('feature', 'dashboard')
#     stats = {
#         'total_traffic': '45,231',
#         'seo_score': '94/100',
#         'page_views': '128,543',
#         'click_rate': '3.24%'
#     }
#     activities = [
#         {'title': 'SEO score improved', 'description': 'Your overall SEO score increased by 5 points', 'icon': 'trending-up', 'color': 'green', 'time': '2 hours ago'},
#         {'title': 'New keyword rankings', 'description': '15 new keywords entered top 10 results', 'icon': 'bar-chart-3', 'color': 'blue', 'time': '5 hours ago'},
#         {'title': 'Traffic milestone reached', 'description': 'Congratulations! You\'ve reached 50K monthly visitors', 'icon': 'users', 'color': 'purple', 'time': '1 day ago'}
#     ]
#     analysis = {}
#     input_text = ''
#     url = ''
#     active_tab = 'keyword'
#
#     if feature == 'content-analyzer' and request.method == 'POST':
#         input_text = request.form.get('content', '').strip()
#         url = request.form.get('url', '').strip()
#         active_tab = request.form.get('active_tab', 'keyword')
#
#         if url:
#             try:
#                 response = requests.get(url, timeout=10)
#                 response.raise_for_status()
#                 input_text = BeautifulSoup(response.text, 'html.parser').get_text()
#             except requests.RequestException as e:
#                 input_text = f"Error fetching URL: {str(e)}"
#
#         if input_text:
#             keywords = extract_keywords(input_text)
#             analysis = {
#                 'keyword_density': [{'name': kw['keyword'], 'density': f"{kw['relevance']*100:.1f}%"} for kw in keywords[:3]],
#                 'keyword_suggestions': [kw['keyword'] for kw in keywords if kw['relevance'] > 0.3][3:6],
#                 'seo_score': seo_score(input_text, {'keywords': keywords}),
#                 'readability': get_readability(input_text),
#                 'grammar_issues': lint_html(input_text),
#                 'summary': {
#                     'key_points': summarize_text(input_text, sentences_count=3).split('<p>')[1:-1],
#                     'auto_summary': summarize_text(input_text, sentences_count=3),
#                 },
#                 'sentiment': sentiment_analysis(input_text),
#                 'content_stats': get_content_stats(input_text),
#             }
#
#     return render_template('dashboard/dashboard.html',
#                          feature=feature,
#                          stats=stats,
#                          activities=activities,
#                          analysis=analysis,
#                          input_text=input_text,
#                          url=url,
#                          active_tab=active_tab)
#
# @dashboard.route('/fetch-content')
# def fetch_content():
#     url = request.args.get('url')
#     if url:
#         try:
#             response = requests.get(url, timeout=10)
#             response.raise_for_status()
#             content = BeautifulSoup(response.text, 'html.parser').get_text()
#             return jsonify({'content': content})
#         except requests.RequestException as e:
#             return jsonify({'error': str(e)}), 400
#     return jsonify({'error': 'No URL provided'}), 400