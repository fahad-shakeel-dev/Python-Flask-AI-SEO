# # # from flask import Blueprint, render_template, request
# # #
# # # main_bp = Blueprint('main', __name__)
# # #
# # # @main_bp.route('/')
# # # def home():
# # #     return render_template('home/index.html')
# # #
# # # @main_bp.route('/features')
# # # def features():
# # #     return render_template('features/features.html')
# # #
# # # @main_bp.route('/about')
# # # def about():
# # #     return render_template('about/about.html')
# # #
# # # @main_bp.route('/contact')
# # # def contact():
# # #     return render_template('contact/contact.html')
# # #
# # # @main_bp.route('/services')
# # # def services():
# # #     return render_template('services/services.html')
# # #
# # # @main_bp.route('/dashboard', methods=['GET', 'POST'])
# # # def dashboard():
# # #     feature = request.args.get('feature', 'dashboard')
# # #     stats = {
# # #         'total_traffic': '45,231',
# # #         'seo_score': '94/100',
# # #         'page_views': '128,543',
# # #         'click_rate': '3.24%'
# # #     }
# # #     activities = [
# # #         {'title': 'SEO score improved', 'description': 'Your overall SEO score increased by 5 points', 'icon': 'trending-up', 'color': 'green', 'time': '2 hours ago'},
# # #         {'title': 'New keyword rankings', 'description': '15 new keywords entered top 10 results', 'icon': 'bar-chart-3', 'color': 'blue', 'time': '5 hours ago'},
# # #         {'title': 'Traffic milestone reached', 'description': 'Congratulations! You\'ve reached 50K monthly visitors', 'icon': 'users', 'color': 'purple', 'time': '1 day ago'}
# # #     ]
# # #     analysis = {}
# # #     input_text = ''
# # #     url = ''
# # #     active_tab = 'keyword'
# # #
# # #     if feature == 'content-analyzer' and request.method == 'POST':
# # #         input_text = request.form.get('content', '')
# # #         url = request.form.get('url', '')
# # #         active_tab = request.form.get('active_tab', 'keyword')
# # #         analysis = {
# # #             'keyword_density': [
# # #                 {'name': 'SEO', 'density': '2.3%'},
# # #                 {'name': 'Content', 'density': '1.8%'},
# # #                 {'name': 'Marketing', 'density': '1.2%'}
# # #             ],
# # #             'keyword_suggestions': ['digital marketing', 'search engine', 'optimization'],
# # #             'seo_score': '85',
# # #             'readability_score': '72/100',
# # #             'grade_level': '8th Grade',
# # #             'stats': {
# # #                 'words': '1,247',
# # #                 'sentences': '68',
# # #                 'paragraphs': '12',
# # #                 'avg_words_sentence': '18.3'
# # #             },
# # #             'grammar_issues': [
# # #                 {'type': 'Spelling Error', 'description': 'Line 5: "recieve" should be "receive"', 'severity': 'red'},
# # #                 {'type': 'Grammar Issue', 'description': 'Line 12: Consider using "who" instead of "that" for people', 'severity': 'yellow'},
# # #                 {'type': 'Style Suggestion', 'description': 'Line 18: Consider using active voice for better readability', 'severity': 'blue'}
# # #             ],
# # #             'summary_points': [
# # #                 'SEO optimization is crucial for online visibility',
# # #                 'Content quality affects search engine rankings',
# # #                 'Regular content updates improve performance'
# # #             ],
# # #             'auto_summary': 'This content discusses the importance of SEO optimization for digital marketing success. It covers key strategies including keyword research, content optimization, and technical SEO improvements that can help websites rank higher in search engine results.',
# # #             'sentiment': {
# # #                 'positive': '65%',
# # #                 'neutral': '25%',
# # #                 'negative': '10%',
# # #                 'overall': 'Positive',
# # #                 'comment': 'Your content has a predominantly positive tone, which is great for engaging readers and building trust.'
# # #             }
# # #         }
# # #
# # #     return render_template('dashboard/dashboard.html',
# # #                          feature=feature,
# # #                          stats=stats,
# # #                          activities=activities,
# # #                          analysis=analysis,
# # #                          input_text=input_text,
# # #                          url=url,
# # #                          active_tab=active_tab)
# #
# #
# #
# #
# #
# #
# #
# #
# # #
# # #
# # #
# # #
# # #
# # #
# # # from flask import Blueprint, render_template, request, flash
# # # import requests
# # # from bs4 import BeautifulSoup
# # # from app.analyzer import (
# # #     extract_keywords, get_readability, grammar_and_spelling,
# # #     summarize_text, sentiment_analysis, seo_score, get_content_stats
# # # )
# # #
# # # main_bp = Blueprint('main', __name__)
# # #
# # # @main_bp.route('/')
# # # def home():
# # #     return render_template('home/index.html')
# # #
# # # @main_bp.route('/features')
# # # def features():
# # #     return render_template('features/features.html')
# # #
# # # @main_bp.route('/about')
# # # def about():
# # #     return render_template('about/about.html')
# # #
# # # @main_bp.route('/contact')
# # # def contact():
# # #     return render_template('contact/contact.html')
# # #
# # # @main_bp.route('/services')
# # # def services():
# # #     return render_template('services/services.html')
# # #
# # # @main_bp.route('/dashboard', methods=['GET', 'POST'])
# # # def dashboard():
# # #     feature = request.args.get('feature', 'dashboard')
# # #     stats = {
# # #         'total_traffic': '45,231',
# # #         'seo_score': '94/100',
# # #         'page_views': '128,543',
# # #         'click_rate': '3.24%'
# # #     }
# # #     activities = [
# # #         {'title': 'SEO score improved', 'description': 'Your overall SEO score increased by 5 points', 'icon': 'trending-up', 'color': 'green', 'time': '2 hours ago'},
# # #         {'title': 'New keyword rankings', 'description': '15 new keywords entered top 10 results', 'icon': 'bar-chart-3', 'color': 'blue', 'time': '5 hours ago'},
# # #         {'title': 'Traffic milestone reached', 'description': 'Congratulations! You\'ve reached 50K monthly visitors', 'icon': 'users', 'color': 'purple', 'time': '1 day ago'}
# # #     ]
# # #     analysis = {
# # #         'keyword_density': [],
# # #         'keyword_suggestions': [],
# # #         'seo_score': '0',
# # #         'readability_score': '0/100',
# # #         'grade_level': 'N/A',
# # #         'stats': {
# # #             'words': '0',
# # #             'sentences': '0',
# # #             'paragraphs': '0',
# # #             'avg_words_sentence': '0'
# # #         },
# # #         'grammar_issues': [{'type': 'No Issues', 'description': 'Enter content to analyze', 'severity': 'green'}],
# # #         'summary_points': [],
# # #         'auto_summary': 'No content provided for summarization.',
# # #         'sentiment': {
# # #             'positive': '0%',
# # #             'neutral': '0%',
# # #             'negative': '0%',
# # #             'overall': 'Neutral',
# # #             'comment': 'No content provided for sentiment analysis.'
# # #         }
# # #     }
# # #     input_text = ''
# # #     url = ''
# # #     active_tab = 'keyword'
# # #     error = None
# # #
# # #     if feature == 'content-analyzer' and request.method == 'POST':
# # #         input_text = request.form.get('content', '').strip()
# # #         url = request.form.get('url', '').strip()
# # #         active_tab = request.form.get('active_tab', 'keyword')
# # #
# # #         # Validate input
# # #         if not input_text and not url:
# # #             error = "Please provide content or a valid URL to analyze."
# # #             flash(error, 'error')
# # #         else:
# # #             # Fetch content from URL if provided, otherwise use input text
# # #             content = input_text
# # #             if url:
# # #                 try:
# # #                     response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
# # #                     response.raise_for_status()
# # #                     soup = BeautifulSoup(response.text, 'html.parser')
# # #                     content = soup.get_text(" ", strip=True)
# # #                 except requests.RequestException as e:
# # #                     error = f"Failed to fetch URL: {str(e)}"
# # #                     flash(error, 'error')
# # #                     content = input_text or ''
# # #
# # #             if content:
# # #                 try:
# # #                     # Perform all analyses
# # #                     keywords = extract_keywords(content, top_n=5)
# # #                     readability = get_readability(content)
# # #                     grammar_result = grammar_and_spelling(content)
# # #                     summary = summarize_text(content, sentences_count=3)
# # #                     sentiment = sentiment_analysis(content)
# # #                     content_stats = get_content_stats(content)
# # #                     seo = seo_score(content, {
# # #                         'keywords': keywords,
# # #                         'readability': readability
# # #                     })
# # #
# # #                     # Structure analysis results for the template
# # #                     analysis = {
# # #                         'keyword_density': [
# # #                             {'name': kw['keyword'], 'density': f"{kw['relevance'] * 100:.1f}%"}
# # #                             for kw in keywords
# # #                         ],
# # #                         'keyword_suggestions': [kw['keyword'] for kw in keywords],
# # #                         'seo_score': f"{seo['score']}",
# # #                         'readability_score': f"{readability['flesch_score']}/100",
# # #                         'grade_level': readability['grade_level'],
# # #                         'stats': {
# # #                             'words': str(content_stats['words']),
# # #                             'sentences': str(content_stats['sentences']),
# # #                             'paragraphs': str(content_stats['paragraphs']),
# # #                             'avg_words_sentence': str(content_stats['avg_words_per_sentence'])
# # #                         },
# # #                         'grammar_issues': [
# # #                             {
# # #                                 'type': 'Correction',
# # #                                 'description': grammar_result,
# # #                                 'severity': 'yellow'
# # #                             } if grammar_result != content else
# # #                             {
# # #                                 'type': 'No Issues',
# # #                                 'description': 'No spelling or grammar issues detected',
# # #                                 'severity': 'green'
# # #                             }
# # #                         ],
# # #                         'summary_points': [point.strip() + ('.' if not point.endswith('.') else '')
# # #                                           for point in summary.split('. ')
# # #                                           if point.strip()],
# # #                         'auto_summary': summary,
# # #                         'sentiment': {
# # #                             'positive': f"{sentiment.get('emotions', {}).get('Positive', 0) * 100:.1f}%"
# # #                                         if 'emotions' in sentiment else f"{70.0 if sentiment['polarity'] > 0 else 0:.1f}%",
# # #                             'neutral': f"{sentiment.get('emotions', {}).get('Neutral', 0) * 100:.1f}%"
# # #                                        if 'emotions' in sentiment else f"{20.0 if abs(sentiment['polarity']) <= 0.05 else 0:.1f}%",
# # #                             'negative': f"{sentiment.get('emotions', {}).get('Negative', 0) * 100:.1f}%"
# # #                                         if 'emotions' in sentiment else f"{10.0 if sentiment['polarity'] < 0 else 0:.1f}%",
# # #                             'overall': sentiment['sentiment'],
# # #                             'comment': f"Your content has a predominantly {sentiment['sentiment'].lower()} tone, which is {'great for engaging readers' if sentiment['sentiment'] == 'Positive' else 'neutral' if sentiment['sentiment'] == 'Neutral' else 'potentially concerning'}."
# # #                         }
# # #                     }
# # #                 except Exception as e:
# # #                     error = f"Analysis failed: {str(e)}"
# # #                     flash(error, 'error')
# # #
# # #     return render_template('dashboard/dashboard.html',
# # #                          feature=feature,
# # #                          stats=stats,
# # #                          activities=activities,
# # #                          analysis=analysis,
# # #                          input_text=input_text,
# # #                          url=url,
# # #                          active_tab=active_tab,
# # #                          error=error)
# # #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # from flask import Blueprint, render_template, request, flash, jsonify
# # import logging
# # from app.keyword_difficulty import get_kd_and_serp
# # from app.analyzer import (
# #     extract_keywords, get_readability, grammar_and_spelling,
# #     summarize_text, sentiment_analysis, seo_score, get_content_stats
# # )
# #
# # # Set up logging
# # logging.basicConfig(level=logging.DEBUG)
# # logger = logging.getLogger(__name__)
# #
# # main_bp = Blueprint('main', __name__)
# #
# # @main_bp.route('/')
# # def home():
# #     return render_template('home/index.html')
# #
# # @main_bp.route('/features')
# # def features():
# #     return render_template('features/features.html')
# #
# # @main_bp.route('/about')
# # def about():
# #     return render_template('about/about.html')
# #
# # @main_bp.route('/contact')
# # def contact():
# #     return render_template('contact/contact.html')
# #
# # @main_bp.route('/services')
# # def services():
# #     return render_template('services/services.html')
# #
# # @main_bp.route('/dashboard', methods=['GET', 'POST'])
# # def dashboard():
# #     feature = request.args.get('feature', 'dashboard')
# #     stats = {
# #         'total_traffic': '45,231',
# #         'seo_score': '94/100',
# #         'page_views': '128,543',
# #         'click_rate': '3.24%'
# #     }
# #     activities = [
# #         {'title': 'SEO score improved', 'description': 'Your overall SEO score increased by 5 points', 'icon': 'trending-up', 'color': 'green', 'time': '2 hours ago'},
# #         {'title': 'New keyword rankings', 'description': '15 new keywords entered top 10 results', 'icon': 'bar-chart-3', 'color': 'blue', 'time': '5 hours ago'},
# #         {'title': 'Traffic milestone reached', 'description': 'Congratulations! You\'ve reached 50K monthly visitors', 'icon': 'users', 'color': 'purple', 'time': '1 day ago'}
# #     ]
# #     analysis = {
# #         'keyword_density': [],
# #         'keyword_suggestions': [],
# #         'seo_score': '0',
# #         'readability_score': '0/100',
# #         'grade_level': 'N/A',
# #         'stats': {
# #             'words': '0',
# #             'sentences': '0',
# #             'paragraphs': '0',
# #             'avg_words_sentence': '0'
# #         },
# #         'grammar_issues': [{'type': 'No Issues', 'description': 'Enter content to analyze', 'severity': 'green'}],
# #         'summary_points': [],
# #         'auto_summary': 'No content provided for summarization.',
# #         'sentiment': {
# #             'positive': '0%',
# #             'neutral': '0%',
# #             'negative': '0%',
# #             'overall': 'Neutral',
# #             'comment': 'No content provided for sentiment analysis.'
# #         }
# #     }
# #     input_text = ''
# #     url = ''
# #     active_tab = 'keyword'
# #     error = None
# #
# #     if feature == 'content-analyzer' and request.method == 'POST':
# #         input_text = request.form.get('content', '').strip()
# #         url = request.form.get('url', '').strip()
# #         active_tab = request.form.get('active_tab', 'keyword')
# #
# #         # Validate input
# #         if not input_text and not url:
# #             error = "Please provide content or a valid URL to analyze."
# #             flash(error, 'error')
# #         else:
# #             # Fetch content from URL if provided, otherwise use input text
# #             content = input_text
# #             if url:
# #                 try:
# #                     response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
# #                     response.raise_for_status()
# #                     soup = BeautifulSoup(response.text, 'html.parser')
# #                     content = soup.get_text(" ", strip=True)
# #                 except requests.RequestException as e:
# #                     error = f"Failed to fetch URL: {str(e)}"
# #                     flash(error, 'error')
# #                     content = input_text or ''
# #
# #             if content:
# #                 try:
# #                     # Perform all analyses
# #                     keywords = extract_keywords(content, top_n=5)
# #                     readability = get_readability(content)
# #                     grammar_result = grammar_and_spelling(content)
# #                     summary = summarize_text(content, sentences_count=3)
# #                     sentiment = sentiment_analysis(content)
# #                     content_stats = get_content_stats(content)
# #                     seo = seo_score(content, {
# #                         'keywords': keywords,
# #                         'readability': readability
# #                     })
# #
# #                     # Structure analysis results for the template
# #                     analysis = {
# #                         'keyword_density': [
# #                             {'name': kw['keyword'], 'density': f"{kw['relevance'] * 100:.1f}%"}
# #                             for kw in keywords
# #                         ],
# #                         'keyword_suggestions': [kw['keyword'] for kw in keywords],
# #                         'seo_score': f"{seo['score']}",
# #                         'readability_score': f"{readability['flesch_score']}/100",
# #                         'grade_level': readability['grade_level'],
# #                         'stats': {
# #                             'words': str(content_stats['words']),
# #                             'sentences': str(content_stats['sentences']),
# #                             'paragraphs': str(content_stats['paragraphs']),
# #                             'avg_words_sentence': str(content_stats['avg_words_per_sentence'])
# #                         },
# #                         'grammar_issues': [
# #                             {
# #                                 'type': 'Correction',
# #                                 'description': grammar_result,
# #                                 'severity': 'yellow'
# #                             } if grammar_result != content else
# #                             {
# #                                 'type': 'No Issues',
# #                                 'description': 'No spelling or grammar issues detected',
# #                                 'severity': 'green'
# #                             }
# #                         ],
# #                         'summary_points': [point.strip() + ('.' if not point.endswith('.') else '')
# #                                           for point in summary.split('. ')
# #                                           if point.strip()],
# #                         'auto_summary': summary,
# #                         'sentiment': {
# #                             'positive': f"{sentiment.get('emotions', {}).get('Positive', 0) * 100:.1f}%"
# #                                         if 'emotions' in sentiment else f"{70.0 if sentiment['polarity'] > 0 else 0:.1f}%",
# #                             'neutral': f"{sentiment.get('emotions', {}).get('Neutral', 0) * 100:.1f}%"
# #                                        if 'emotions' in sentiment else f"{20.0 if abs(sentiment['polarity']) <= 0.05 else 0:.1f}%",
# #                             'negative': f"{sentiment.get('emotions', {}).get('Negative', 0) * 100:.1f}%"
# #                                         if 'emotions' in sentiment else f"{10.0 if sentiment['polarity'] < 0 else 0:.1f}%",
# #                             'overall': sentiment['sentiment'],
# #                             'comment': f"Your content has a predominantly {sentiment['sentiment'].lower()} tone, which is {'great for engaging readers' if sentiment['sentiment'] == 'Positive' else 'neutral' if sentiment['sentiment'] == 'Neutral' else 'potentially concerning'}."
# #                         }
# #                     }
# #                 except Exception as e:
# #                     error = f"Analysis failed: {str(e)}"
# #                     flash(error, 'error')
# #
# #     return render_template('dashboard/dashboard.html',
# #                          feature=feature,
# #                          stats=stats,
# #                          activities=activities,
# #                          analysis=analysis,
# #                          input_text=input_text,
# #                          url=url,
# #                          active_tab=active_tab,
# #                          error=error)
# #
# # @main_bp.route('/api/keyword-difficulty', methods=['POST'])
# # def keyword_difficulty():
# #     try:
# #         payload = request.get_json(silent=True) or {}
# #         logger.debug(f"Received request: {payload}")
# #         keyword = payload.get('keyword', '').strip()
# #         country = payload.get('country', 'us').strip()
# #
# #         if not keyword:
# #             logger.warning("Keyword is required")
# #             return jsonify({'ok': False, 'error': 'Keyword is required'}), 400
# #
# #         logger.info(f"Fetching data for keyword: {keyword}, country: {country}")
# #         result = get_kd_and_serp(keyword, country)
# #         logger.debug(f"API response: {result}")
# #         return jsonify({'ok': True, **result}), 200
# #     except RuntimeError as e:
# #         logger.error(f"KD API error: {str(e)}")
# #         return jsonify({'ok': False, 'error': str(e)}), 502
# #     except Exception as e:
# #         logger.error(f"Unexpected error: {str(e)}", exc_info=True)
# #         return jsonify({'ok': False, 'error': 'An unexpected error occurred'}), 500
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from flask import Blueprint, render_template, request, jsonify
# import logging
# from app.site_audit import run_pagespeed, extract_all
# from app.keyword_difficulty import get_kd_and_serp
# from app.analyzer import (
#     extract_keywords, get_readability, grammar_and_spelling,
#     summarize_text, sentiment_analysis, seo_score, get_content_stats, run_gap_analysis
# )
# from app.models.middleware import login_required
# # Set up logging
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
#
# main_bp = Blueprint('main', __name__)
#
# @main_bp.route('/')
# def home():
#     return render_template('home/index.html')
#
# @main_bp.route('/features')
# def features():
#     return render_template('features/features.html')
#
# @main_bp.route('/about')
# def about():
#     return render_template('about/about.html')
#
# @main_bp.route('/contact')
# def contact():
#     return render_template('contact/contact.html')
#
# @main_bp.route('/services')
# def services():
#     return render_template('services/services.html')
#
# @main_bp.route('/dashboard', methods=['GET', 'POST'])
# @login_required
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
#     analysis = {
#         'keyword_density': [],
#         'keyword_suggestions': [],
#         'seo_score': '0',
#         'readability_score': '0/100',
#         'grade_level': 'N/A',
#         'stats': {
#             'words': '0',
#             'sentences': '0',
#             'paragraphs': '0',
#             'avg_words_sentence': '0'
#         },
#         'grammar_issues': [{'type': 'No Issues', 'description': 'Enter content to analyze', 'severity': 'green'}],
#         'summary_points': [],
#         'auto_summary': 'No content provided for summarization.',
#         'sentiment': {
#             'positive': '0%',
#             'neutral': '0%',
#             'negative': '0%',
#             'overall': 'Neutral',
#             'comment': 'No content provided for sentiment analysis.'
#         }
#     }
#     input_text = ''
#     url = ''
#     active_tab = 'keyword'
#     error = None
#
#     if feature == 'content-analyzer' and request.method == 'POST':
#         input_text = request.form.get('content', '').strip()
#         url = request.form.get('url', '').strip()
#         active_tab = request.form.get('active_tab', 'keyword')
#
#         # Validate input
#         if not input_text and not url:
#             error = "Please provide content or a valid URL to analyze."
#             flash(error, 'error')
#         else:
#             # Fetch content from URL if provided, otherwise use input text
#             content = input_text
#             if url:
#                 try:
#                     response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
#                     response.raise_for_status()
#                     soup = BeautifulSoup(response.text, 'html.parser')
#                     content = soup.get_text(" ", strip=True)
#                 except requests.RequestException as e:
#                     error = f"Failed to fetch URL: {str(e)}"
#                     flash(error, 'error')
#                     content = input_text or ''
#
#             if content:
#                 try:
#                     # Perform all analyses
#                     keywords = extract_keywords(content, top_n=5)
#                     readability = get_readability(content)
#                     grammar_result = grammar_and_spelling(content)
#                     summary = summarize_text(content, sentences_count=3)
#                     sentiment = sentiment_analysis(content)
#                     content_stats = get_content_stats(content)
#                     seo = seo_score(content, {
#                         'keywords': keywords,
#                         'readability': readability
#                     })
#
#                     # Structure analysis results for the template
#                     analysis = {
#                         'keyword_density': [
#                             {'name': kw['keyword'], 'density': f"{kw['relevance'] * 100:.1f}%"}
#                             for kw in keywords
#                         ],
#                         'keyword_suggestions': [kw['keyword'] for kw in keywords],
#                         'seo_score': f"{seo['score']}",
#                         'readability_score': f"{readability['flesch_score']}/100",
#                         'grade_level': readability['grade_level'],
#                         'stats': {
#                             'words': str(content_stats['words']),
#                             'sentences': str(content_stats['sentences']),
#                             'paragraphs': str(content_stats['paragraphs']),
#                             'avg_words_sentence': str(content_stats['avg_words_per_sentence'])
#                         },
#                         'grammar_issues': [
#                             {
#                                 'type': 'Correction',
#                                 'description': grammar_result,
#                                 'severity': 'yellow'
#                             } if grammar_result != content else
#                             {
#                                 'type': 'No Issues',
#                                 'description': 'No spelling or grammar issues detected',
#                                 'severity': 'green'
#                             }
#                         ],
#                         'summary_points': [point.strip() + ('.' if not point.endswith('.') else '')
#                                           for point in summary.split('. ')
#                                           if point.strip()],
#                         'auto_summary': summary,
#                         'sentiment': {
#                             'positive': f"{sentiment.get('emotions', {}).get('Positive', 0) * 100:.1f}%"
#                                         if 'emotions' in sentiment else f"{70.0 if sentiment['polarity'] > 0 else 0:.1f}%",
#                             'neutral': f"{sentiment.get('emotions', {}).get('Neutral', 0) * 100:.1f}%"
#                                        if 'emotions' in sentiment else f"{20.0 if abs(sentiment['polarity']) <= 0.05 else 0:.1f}%",
#                             'negative': f"{sentiment.get('emotions', {}).get('Negative', 0) * 100:.1f}%"
#                                         if 'emotions' in sentiment else f"{10.0 if sentiment['polarity'] < 0 else 0:.1f}%",
#                             'overall': sentiment['sentiment'],
#                             'comment': f"Your content has a predominantly {sentiment['sentiment'].lower()} tone, which is {'great for engaging readers' if sentiment['sentiment'] == 'Positive' else 'neutral' if sentiment['sentiment'] == 'Neutral' else 'potentially concerning'}."
#                         }
#                     }
#                 except Exception as e:
#                     error = f"Analysis failed: {str(e)}"
#                     flash(error, 'error')
#
#     return render_template('dashboard/dashboard.html',
#                          feature=feature,
#                          stats=stats,
#                          activities=activities,
#                          analysis=analysis,
#                          input_text=input_text,
#                          url=url,
#                          active_tab=active_tab,
#                          error=error)
#
# @main_bp.route('/api/keyword-difficulty', methods=['POST'])
# def keyword_difficulty():
#     try:
#         payload = request.get_json(silent=True) or {}
#         logger.debug(f"Received request: {payload}")
#         keyword = payload.get('keyword', '').strip()
#         country = payload.get('country', 'us').strip()
#
#         if not keyword:
#             logger.warning("Keyword is required")
#             return jsonify({'ok': False, 'error': 'Keyword is required'}), 400
#
#         logger.info(f"Fetching data for keyword: {keyword}, country: {country}")
#         result = get_kd_and_serp(keyword, country)
#         logger.debug(f"API response: {result}")
#         return jsonify({'ok': True, **result}), 200
#     except RuntimeError as e:
#         logger.error(f"KD API error: {str(e)}")
#         return jsonify({'ok': False, 'error': str(e)}), 502
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}", exc_info=True)
#         return jsonify({'ok': False, 'error': 'An unexpected error occurred'}), 500
#
#
# @main_bp.route('/audit', methods=['GET', 'POST'])
# def audit():
#     if request.method == 'POST':
#         data = request.get_json(silent=True) or {}
#         print(f"Received: {data}") # Debug log
#
#         url = data.get('url', '').strip()
#         device = data.get('device', 'desktop').lower()
#
#         print(f"URL: {url}, Device: {device}") # Extra debug
#
#         if not url:
#             return jsonify({'error': 'Please enter a valid URL'}), 400
#
#         try:
#             data = run_pagespeed(url, strategy=device)
#             results = extract_all(data)
#             return jsonify({
#                 'ok': True,
#                 'results': results,
#                 'device': device
#             })
#         except Exception as e:
#             return jsonify({'ok': False, 'error': str(e)}), 500
#
#     return render_template('site_audit.html')
#
#
#
#
#
# @main_bp.route('/gap-analysis', methods=['POST'])
# def gap_analysis():
#     data = request.get_json(silent=True) or {}
#     print(f"Received: {data}") # Debug log
#
#     keyword = data.get('keyword', '').strip()
#     content = data.get('content', '').strip()
#
#     if not keyword or not content:
#         return jsonify({'error': 'Please provide both keyword and content'}), 400
#
#     try:
#         result = run_gap_analysis(keyword, content)
#         return jsonify({'ok': True, 'result': result})
#     except Exception as e:
#         return jsonify({'ok': False, 'error': str(e)}), 500
















from flask import Blueprint, render_template, request, flash, jsonify
import logging
import aiohttp
import asyncio
from aiohttp import ClientSession
from app.site_audit import run_pagespeed, extract_all
from app.keyword_difficulty import get_kd_and_serp
from app.analyzer import (
    extract_keywords, get_readability, grammar_and_spelling,
    summarize_text, sentiment_analysis, seo_score, get_content_stats, run_gap_analysis,
    get_cached_analysis, set_cached_analysis
)
from app.models.middleware import login_required
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('home/index.html')

@main_bp.route('/features')
def features():
    return render_template('features/features.html')

@main_bp.route('/about')
def about():
    return render_template('about/about.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact/contact.html')

@main_bp.route('/services')
def services():
    return render_template('services/services.html')

async def fetch_url_content(url: str) -> str:
    async with ClientSession(headers={'User-Agent': 'Mozilla/5.0'}) as session:
        async with session.get(url, timeout=10) as response:
            response.raise_for_status()
            text = await response.text()
            soup = BeautifulSoup(text[:100000], 'html.parser')  # Limit to 100KB
            return soup.get_text(" ", strip=True)

def run_analysis_task(func, *args, **kwargs):
    return func(*args, **kwargs)

@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    feature = request.args.get('feature', 'dashboard')
    stats = {
        'total_traffic': '45,231',
        'seo_score': '94/100',
        'page_views': '128,543',
        'click_rate': '3.24%'
    }
    activities = [
        {'title': 'SEO score improved', 'description': 'Your overall SEO score increased by 5 points', 'icon': 'trending-up', 'color': 'green', 'time': '2 hours ago'},
        {'title': 'New keyword rankings', 'description': '15 new keywords entered top 10 results', 'icon': 'bar-chart-3', 'color': 'blue', 'time': '5 hours ago'},
        {'title': 'Traffic milestone reached', 'description': 'Congratulations! You\'ve reached 50K monthly visitors', 'icon': 'users', 'color': 'purple', 'time': '1 day ago'}
    ]
    analysis = {
        'keyword_density': [],
        'keyword_suggestions': [],
        'seo_score': '0',
        'readability_score': '0/100',
        'grade_level': 'N/A',
        'stats': {
            'words': '0',
            'sentences': '0',
            'paragraphs': '0',
            'avg_words_sentence': '0'
        },
        'grammar_issues': [{'type': 'No Issues', 'description': 'Enter content to analyze', 'severity': 'green'}],
        'summary_points': [],
        'auto_summary': 'No content provided for summarization.',
        'sentiment': {
            'positive': '0%',
            'neutral': '0%',
            'negative': '0%',
            'overall': 'Neutral',
            'comment': 'No content provided for sentiment analysis.'
        }
    }
    input_text = ''
    url = ''
    active_tab = 'keyword'
    error = None

    if feature == 'content-analyzer' and request.method == 'POST':
        input_text = request.form.get('content', '').strip()
        url = request.form.get('url', '').strip()
        active_tab = request.form.get('active_tab', 'keyword')

        if not input_text and not url:
            error = "Please provide content or a valid URL to analyze."
            flash(error, 'error')
        else:
            content = input_text
            if url:
                try:
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    content = loop.run_until_complete(fetch_url_content(url))
                    loop.close()
                except Exception as e:
                    error = f"Failed to fetch URL: {str(e)}"
                    flash(error, 'error')
                    content = input_text or ''

            if content:
                try:
                    cached_result = get_cached_analysis(content, url)
                    if cached_result:
                        analysis = cached_result
                    else:
                        with ThreadPoolExecutor(max_workers=5) as executor:
                            futures = [
                                executor.submit(run_analysis_task, extract_keywords, content, top_n=3),
                                executor.submit(run_analysis_task, get_readability, content),
                                executor.submit(run_analysis_task, grammar_and_spelling, content),
                                executor.submit(run_analysis_task, summarize_text, content, sentences_count=3),
                                executor.submit(run_analysis_task, sentiment_analysis, content),
                                executor.submit(run_analysis_task, get_content_stats, content)
                            ]
                            keywords, readability, grammar_result, summary, sentiment, content_stats = [f.result() for f in futures]

                            seo = seo_score(content, {
                                'keywords': keywords,
                                'readability': readability
                            })

                            analysis = {
                                'keyword_density': [
                                    {'name': kw['keyword'], 'density': f"{kw['relevance'] * 100:.1f}%"}
                                    for kw in keywords
                                ],
                                'keyword_suggestions': [kw['keyword'] for kw in keywords],
                                'seo_score': f"{seo['score']}",
                                'readability_score': f"{readability['flesch_score']}/100",
                                'grade_level': readability['grade_level'],
                                'stats': {
                                    'words': str(content_stats['words']),
                                    'sentences': str(content_stats['sentences']),
                                    'paragraphs': str(content_stats['paragraphs']),
                                    'avg_words_sentence': str(content_stats['avg_words_per_sentence'])
                                },
                                'grammar_issues': [
                                    {
                                        'type': 'Correction',
                                        'description': grammar_result,
                                        'severity': 'yellow'
                                    } if grammar_result != content else
                                    {
                                        'type': 'No Issues',
                                        'description': 'No spelling or grammar issues detected',
                                        'severity': 'green'
                                    }
                                ],
                                'summary_points': [point.strip() + ('.' if not point.endswith('.') else '')
                                                  for point in summary.split('. ')
                                                  if point.strip()],
                                'auto_summary': summary,
                                'sentiment': {
                                    'positive': f"{sentiment.get('emotions', {}).get('Positive', 0) * 100:.1f}%",
                                    'neutral': f"{sentiment.get('emotions', {}).get('Neutral', 0) * 100:.1f}%",
                                    'negative': f"{sentiment.get('emotions', {}).get('Negative', 0) * 100:.1f}%",
                                    'overall': sentiment['sentiment'],
                                    'comment': f"Your content has a predominantly {sentiment['sentiment'].lower()} tone, which is {'great for engaging readers' if sentiment['sentiment'] == 'Positive' else 'neutral' if sentiment['sentiment'] == 'Neutral' else 'potentially concerning'}."
                                }
                            }
                            set_cached_analysis(content, url, analysis)
                except Exception as e:
                    error = f"Analysis failed: {str(e)}"
                    flash(error, 'error')

    return render_template('dashboard/dashboard.html',
                         feature=feature,
                         stats=stats,
                         activities=activities,
                         analysis=analysis,
                         input_text=input_text,
                         url=url,
                         active_tab=active_tab,
                         error=error)

@main_bp.route('/api/keyword-difficulty', methods=['POST'])
def keyword_difficulty():
    try:
        payload = request.get_json(silent=True) or {}
        logger.debug(f"Received request: {payload}")
        keyword = payload.get('keyword', '').strip()
        country = payload.get('country', 'us').strip()

        if not keyword:
            logger.warning("Keyword is required")
            return jsonify({'ok': False, 'error': 'Keyword is required'}), 400

        logger.info(f"Fetching data for keyword: {keyword}, country: {country}")
        result = get_kd_and_serp(keyword, country)
        logger.debug(f"API response: {result}")
        return jsonify({'ok': True, **result}), 200
    except RuntimeError as e:
        logger.error(f"KD API error: {str(e)}")
        return jsonify({'ok': False, 'error': str(e)}), 502
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}", exc_info=True)
        return jsonify({'ok': False, 'error': 'An unexpected error occurred'}), 500

@main_bp.route('/audit', methods=['GET', 'POST'])
def audit():
    if request.method == 'POST':
        data = request.get_json(silent=True) or {}
        logger.debug(f"Received: {data}")
        url = data.get('url', '').strip()
        device = data.get('device', 'desktop').lower()

        if not url:
            return jsonify({'error': 'Please enter a valid URL'}), 400

        try:
            data = run_pagespeed(url, strategy=device)
            results = extract_all(data)
            return jsonify({
                'ok': True,
                'results': results,
                'device': device
            })
        except Exception as e:
            return jsonify({'ok': False, 'error': str(e)}), 500

    return render_template('site_audit.html')

@main_bp.route('/gap-analysis', methods=['POST'])
def gap_analysis():
    data = request.get_json(silent=True) or {}
    logger.debug(f"Received: {data}")
    keyword = data.get('keyword', '').strip()
    content = data.get('content', '').strip()

    if not keyword or not content:
        return jsonify({'error': 'Please provide both keyword and content'}), 400

    try:
        result = run_gap_analysis(keyword, content)
        return jsonify({'ok': True, 'result': result})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e)}), 500