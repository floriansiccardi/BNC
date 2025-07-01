conv_ascii_str = {
    ' ': '%SPC%',
    '-': '%DSH%'
}

def ascii2str(ascii: str) -> str:
    for rpl_, by_ in conv_ascii_str.items():
        ascii = ascii.replace(rpl_,  by_)
    return ascii

def str2ascii(str_: str) -> str:
    for by_, rpl_ in conv_ascii_str.items():
        str_ = str_.replace(rpl_,  by_)
    return str_