from flask import Blueprint, render_template, request, jsonify
from .analyzer import extract_keywords, get_readability, grammar_and_spelling, summarize_text, sentiment_analysis, seo_score, lint_html, get_content_stats
import requests
from bs4 import BeautifulSoup

dashboard = Blueprint('dashboard', __name__)

@dashboard.route('/content-analyzer', methods=['GET', 'POST'])
def content_analyzer():
    content_input = ''
    url_input = ''
    analysis_results = None
    active_tab = request.args.get('tab', 'keyword')

    if request.method == 'POST':
        content_input = request.form.get('content_input', '').strip()
        url_input = request.form.get('url_input', '').strip()

        if url_input:
            try:
                response = requests.get(url_input, timeout=10)
                response.raise_for_status()
                content_input = BeautifulSoup(response.text, 'html.parser').get_text()
            except requests.RequestException as e:
                content_input = f"Error fetching URL: {str(e)}"

        if content_input:
            analysis_results = {
                'keyword_density': {kw['keyword']: kw['relevance'] for kw in extract_keywords(content_input)[:3]},
                'keyword_suggestions': [kw['keyword'] for kw in extract_keywords(content_input) if kw['relevance'] > 0.3][3:6],
                'seo_score': seo_score(content_input, {'keywords': extract_keywords(content_input)}),
                'readability': get_readability(content_input),
                'grammar_issues': lint_html(content_input),
                'summary': {
                    'key_points': summarize_text(content_input, sentences_count=3).split('<p>')[1:-1],
                    'auto_summary': summarize_text(content_input, sentences_count=3),
                },
                'sentiment': sentiment_analysis(content_input),
                'content_stats': get_content_stats(content_input),
            }

    return render_template('partials/dashboard/content-analyzer.html', content_input=content_input, url_input=url_input, analysis_results=analysis_results, active_tab=active_tab)

@dashboard.route('/fetch-content')
def fetch_content():
    url = request.args.get('url')
    if url:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            content = BeautifulSoup(response.text, 'html.parser').get_text()
            return jsonify({'content': content})
        except requests.RequestException as e:
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'No URL provided'}), 400