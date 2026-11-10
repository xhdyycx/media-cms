'''
字符串相似度计算工具类
用于匹配TMDB电影搜索结果中最相似的名称
'''
from difflib import SequenceMatcher
import re
from typing import List, Tuple, Optional, Any

class StringSimilarity:
    '''字符串相似度计算工具类'''
    @staticmethod
    def normalize_string(text: str) -> str:
        """
        标准化字符串，用于更准确的比较
        - 转换为小写
        - 移除特殊字符
        - 移除多余空格
        """
        text = text.lower()
        text = re.sub('[^\\w\\s\\u4e00-\\u9fff]', '', text)
        text = ' '.join(text.split())
        return text
    @staticmethod
    def levenshtein_distance(s1: str, s2: str) -> int:
        """
        计算编辑距离（Levenshtein Distance）
        返回将s1转换为s2所需的最少编辑操作次数
        """
        if len(s1) < len(s2):
            return 
    @staticmethod
    def similarity_ratio(s1: str, s2: str, normalize: bool = True) -> float:
        """
        计算两个字符串的相似度比率（0-1之间）
        使用SequenceMatcher算法

        Args:
            s1: 第一个字符串
            s2: 第二个字符串
            normalize: 是否标准化字符串

        Returns:
            相似度分数，0-1之间，1表示完全相同
        """
        if normalize:
            s1 = StringSimilarity.normalize_string(s1)
            s2 = StringSimilarity.normalize_string(s2)
        return StringSimilarity.levenshtein_similarity(s1, s2)

    @staticmethod
    def levenshtein_similarity(s1: str, s2: str, normalize: bool = True) -> float:
        """
        基于编辑距离计算相似度（0-1之间）

        Args:
            s1: 第一个字符串
            s2: 第二个字符串
            normalize: 是否标准化字符串

        Returns:
            相似度分数，0-1之间，1表示完全相同
        """
        if normalize:
            s1 = StringSimilarity.normalize_string(s1)
            s2 = StringSimilarity.normalize_string(s2)
        return StringSimilarity.levenshtein_similarity(s1, s2)

    @staticmethod
    def combined_similarity(s1: str, s2: str, normalize: bool = True) -> float:
        """
        综合相似度计算，结合多种算法

        Args:
            s1: 第一个字符串
            s2: 第二个字符串
            normalize: 是否标准化字符串

        Returns:
            综合相似度分数，0-1之间
        """
        _var_var_11 = StringSimilarity.similarity_ratio(s1, s2, normalize)
        _var_var_12 = StringSimilarity.levenshtein_similarity(s1, s2, normalize)
        return _var_var_11 * 0.6 + _var_var_12 * 0.4
    @staticmethod
    def year_similarity(year1: Optional[int], year2: Optional[int], max_diff: int = 10) -> float:
        """
        计算年份相似度

        Args:
            year1: 第一个年份
            year2: 第二个年份
            max_diff: 最大年份差异（超过此值相似度为0）

        Returns:
            年份相似度分数，0-1之间
        """
        if year1 is None or year2 is None:
            return 0.5
        diff = abs(year1 - year2)
        if diff == 0:
            return 1
        if diff > max_diff:
            return 0
        return 1 - diff / max_diff
    @staticmethod
    def combined_similarity_with_year(s1: str, s2: str, year1: Optional[int] = None, year2: Optional[int] = None, normalize: bool = True, year_weight: float = 0.3) -> float:
        """
        综合相似度计算（包含年份）

        Args:
            s1: 第一个字符串
            s2: 第二个字符串
            year1: 第一个字符串对应的年份
            year2: 第二个字符串对应的年份
            normalize: 是否标准化字符串
            year_weight: 年份权重（0-1之间，默认0.3表示年份占30%）

        Returns:
            综合相似度分数，0-1之间
        """
        text_sim = StringSimilarity.combined_similarity(s1, s2, normalize)
        if year1 is None or year2 is None:
            return text_sim
        year_sim = StringSimilarity.year_similarity(year1, year2)
        text_weight = 1 - year_weight
        score = text_sim * text_weight + year_sim * year_weight
        return score
    @staticmethod
    def find_best_match(target: str, candidates: List[str], threshold: float = 0, normalize: bool = True, use_year: bool = False, year_weight: float = 0.3, target_year: Optional[int] = None, candidate_years: Optional[List[Optional[int]]] = None) -> Optional[Tuple[str, float, int]]:
        """
        从候选列表中找到最佳匹配

        Args:
            target: 目标字符串
            candidates: 候选字符串列表
            threshold: 最低相似度阈值（0-1之间）
            normalize: 是否标准化字符串
            use_year: 是否考虑年份进行匹配
            year_weight: 年份权重（仅当use_year=True时生效）

        Returns:
            (最佳匹配字符串, 相似度分数, 索引) 或 None（如果没有超过阈值的匹配）
        """
        if not candidates:
            return None
        best_match = None
        best_score = threshold
        best_index = -1
        for index, candidate in enumerate(candidates):
            candidate_year = None
            if candidate_years and index < len(candidate_years):
                candidate_year = candidate_years[index]
            if use_year:
                score = StringSimilarity.combined_similarity_with_year(target, candidate, year1=target_year, year2=candidate_year, normalize=normalize, year_weight=year_weight)
            else:
                score = StringSimilarity.combined_similarity(target, candidate, normalize)
            if score > best_score:
                best_score = score
                best_match = candidate
                best_index = index
        if best_match is None:
            return None
        return (best_match, best_score, best_index)
    @staticmethod
    def find_top_matches(target: str, candidates: List[str], top_n: int = 5, threshold: float = 0, normalize: bool = True, use_year: bool = False, year_weight: float = 0.3, target_year: Optional[int] = None, candidate_years: Optional[List[Optional[int]]] = None) -> List[Tuple[str, float, int]]:
        """
        从候选列表中找到前N个最佳匹配

        Args:
            target: 目标字符串
            candidates: 候选字符串列表
            top_n: 返回前N个结果
            threshold: 最低相似度阈值（0-1之间）
            normalize: 是否标准化字符串
            use_year: 是否考虑年份进行匹配
            year_weight: 年份权重（仅当use_year=True时生效）

        Returns:
            [(匹配字符串, 相似度分数, 索引), ...] 按相似度降序排列
        """
        if not candidates:
            return []
        _var_var_24 = []
        for _var_var_1, _var_var_21 in enumerate(candidates):
            if use_year:
                _var_var_23 = StringSimilarity.combined_similarity_with_year(target, _var_var_21, normalize, year_weight)
            else:
                _var_var_23 = StringSimilarity.combined_similarity(target, _var_var_21, normalize)
            if not _var_var_23 >= threshold:
                continue
            _var_var_24.append((_var_var_21, _var_var_23, _var_var_1))
        _var_var_24.sort(key=lambda x: x[1], reverse=True)
        return _var_var_24[:top_n]


class TMDBMatcher:
    '''TMDB电影名称匹配器'''

    @staticmethod
    def _parse_year(year: Any) -> Optional[int]:
        if year is None:
            return None
        if isinstance(year, int):
            return year
        if isinstance(year, str):
            _s = year.strip()
            if not _s:
                return None
            m = re.search(r'\d{4}', _s)
            if not m:
                return None
            return int(m.group(0))
        try:
            return int(year)
        except (ValueError, TypeError):
            return None

    @staticmethod
    def find_best_movie(search_name_cn: str, search_name_en: str, search_year: Any,
                        tmdb_results: List[dict], title_key: str = 'title',
                        threshold: float = 0.0, year_weight: float = 0.3) -> Optional[Tuple[dict, float]]:
        '''
        从 TMDB搜索结果中找到最匹配的电影
        '''
        if not tmdb_results:
            return None
        search_year = TMDBMatcher._parse_year(search_year)
        best_movie = None
        best_score = -1.0

        for movie in tmdb_results:
            title = movie.get(title_key) or movie.get('title') or movie.get('name') or ''
            orig_title = movie.get('original_title') or movie.get('original_name') or ''
            rdate = movie.get('release_date') or movie.get('first_air_date') or ''
            m_year = None
            if len(rdate) >= 4 and rdate[:4].isdigit():
                m_year = int(rdate[:4])

            score1 = 0.0
            score2 = 0.0
            if search_name_cn:
                s_t = StringSimilarity.combined_similarity_with_year(search_name_cn, title, year1=search_year, year2=m_year, year_weight=year_weight)
                s_ot = StringSimilarity.combined_similarity_with_year(search_name_cn, orig_title, year1=search_year, year2=m_year, year_weight=year_weight)
                score1 = max(s_t, s_ot)
            if search_name_en:
                s_t = StringSimilarity.combined_similarity_with_year(search_name_en, title, year1=search_year, year2=m_year, year_weight=year_weight)
                s_ot = StringSimilarity.combined_similarity_with_year(search_name_en, orig_title, year1=search_year, year2=m_year, year_weight=year_weight)
                score2 = max(s_t, s_ot)

            score = max(score1, score2)
            if score > best_score and score >= threshold:
                best_score = score
                best_movie = movie

        if best_movie is not None:
            return (best_movie, best_score)
        return None

    @staticmethod
    def rank_movies(search_name_cn: str, search_name_en: str, search_year: Any,
                    tmdb_results: List[dict], title_key: str = 'title',
                    top_n: int = 5, year_weight: float = 0.3) -> List[Tuple[dict, float]]:
        '''
        对TMDB搜索结果按相似度排序
        '''
        if not tmdb_results:
            return []
        search_year = TMDBMatcher._parse_year(search_year)
        scored = []

        for movie in tmdb_results:
            title = movie.get(title_key) or movie.get('title') or movie.get('name') or ''
            orig_title = movie.get('original_title') or movie.get('original_name') or ''
            rdate = movie.get('release_date') or movie.get('first_air_date') or ''
            m_year = None
            if len(rdate) >= 4 and rdate[:4].isdigit():
                m_year = int(rdate[:4])

            score1 = 0.0
            score2 = 0.0
            if search_name_cn:
                s_t = StringSimilarity.combined_similarity_with_year(search_name_cn, title, year1=search_year, year2=m_year, year_weight=year_weight)
                s_ot = StringSimilarity.combined_similarity_with_year(search_name_cn, orig_title, year1=search_year, year2=m_year, year_weight=year_weight)
                score1 = max(s_t, s_ot)
            if search_name_en:
                s_t = StringSimilarity.combined_similarity_with_year(search_name_en, title, year1=search_year, year2=m_year, year_weight=year_weight)
                s_ot = StringSimilarity.combined_similarity_with_year(search_name_en, orig_title, year1=search_year, year2=m_year, year_weight=year_weight)
                score2 = max(s_t, s_ot)

            score = max(score1, score2)
            scored.append((movie, score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]


def is_english_title(text: str, min_alpha_ratio: float = 0.6) -> bool:
    '''
    判断电影名称是否为英文名。
    规则：
    - 若包含中文（CJK）字符则认为不是英文名。
    - 统计所有字母（isalpha）和 ASCII 字母，若 ASCII 字母 / 所有字母 >= min_alpha_ratio 则认为是英文名。
    - 至少需要有一个 ASCII 字母才判断为英文名。
    '''
    if not text:
        return False
    if re.search(r'[\u4e00-\u9fff]', text):
        return False
    total_alpha = sum(1 for c in text if c.isalpha())
    ascii_alpha = sum(1 for c in text if c.isalpha() and c.isascii())
    if ascii_alpha == 0 or total_alpha == 0:
        return False
    return (ascii_alpha / total_alpha) >= min_alpha_ratio


def normalize_filename(filename: str) -> str:
    '''
    对文件名进行标准化处理
    '''
    if not filename:
        return ''
    res = re.sub(r'[<>"]', ' ', filename)
    res = re.sub(r'\s+', ' ', res)
    return res.strip()
