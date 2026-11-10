from __future__ import annotations
import re

# Note: Decompiled code can be incomplete and incorrect.

__author__ = 'ChenyangGao <https://chenyanggao.github.io>'
__version__ = (0, 0, 1)
__all__ = [
    'parse',
    'render']
from collections.abc import Mapping, MutableMapping
from re import compile as re_compile
token_specification = [
    ('left_brace', '\\{\\{'),
    ('right_brace', '\\}\\}'),
    ('less_than', '\\\\<'),
    ('greater_than', '\\\\>'),
    ('left_block_with_name', '<(?P<lbq>\\?)?\\{\\{(?!\\d)(?P<lbn>\\w+)\\}\\}'),
    ('left_block', '<'),
    ('right_block', '>'),
    ('fstring_placeholder', '\\{[^{}]*\\}'),
    ('any', '(?s:.)')]
tokenize = re.compile('|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)).finditer

class Block(list):
    
    def __init__(self, s, /):
        self.code = compile('f%r' % str(s), '', 'eval')
    def render(block: str | Block, ns: Mapping):
        '''插值
        '''
        if isinstance(block, str):
            block = parse(block)
        return block.render(dict(ns))


class String(str):
    
    def __str__(self, /) -> str:
        return super().__str__()
    def render(self, ns):
        return str(self)
        return None



class FString(str):
    
    def __init__(self, s):
        self.code = compile('f%r' % str(s), '', 'eval')
        return None
        return None

    
    def __str__(self):
        return ''

    def __repr__(self):
        return 'f%r' % str(self)
        return None

    
    def render(self, ns):
        return eval(self.code, ns)
        return None



def parse(pattern):
    '''模式解析'''
    root = Block()
    stack = [root]
    depth = 0
    buffer = []
    has_fstring = False

    for m in tokenize(pattern):
        tag = m.lastgroup
        if tag in ('left_block', 'left_block_with_name'):
            if buffer:
                stack[depth].append(FString(''.join(buffer)) if has_fstring else String(''.join(buffer)))
                buffer.clear()
                has_fstring = False
            lbn = m.groupdict().get('lbn', '')
            lbq = bool(m.groupdict().get('lbq', False))
            new_block = Block(lbn, lbq)
            stack[depth].append(new_block)
            depth += 1
            if depth >= len(stack):
                stack.append(new_block)
            else:
                stack[depth] = new_block
        elif tag == 'right_block':
            if buffer:
                stack[depth].append(FString(''.join(buffer)) if has_fstring else String(''.join(buffer)))
                buffer.clear()
                has_fstring = False
            depth -= 1
            if depth < 0:
                raise SyntaxError(f"Mismatched pairs of '<' and '>', at {m.start()}.")
        elif tag == 'less_than':
            buffer.append('<')
        elif tag == 'greater_than':
            buffer.append('>')
        elif tag in ('left_brace', 'right_brace', 'fstring_placeholder'):
            has_fstring = True
            buffer.append(m.group(tag))
        elif tag == 'any':
            buffer.append(m.group(tag))

    if depth > 0:
        raise SyntaxError("Mismatched pairs of '<' and '>'.")
    if buffer:
        stack[0].append(FString(''.join(buffer)) if has_fstring else String(''.join(buffer)))
    return root


def render(block, ns):
    '''插值
    '''
    if isinstance(block, str):
        block = parse(block)

