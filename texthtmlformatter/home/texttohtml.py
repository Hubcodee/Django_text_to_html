# -*- coding: utf-8 -*-
import re


def formatHtml(text):
    # Remove Windows Linebreaks
    text = text.replace('\r\n', '\n')

    # Replace  H1
    text = re.sub('(\n/(?!/))(?P<id>.+)', '<h1>\g<id></h1>', text, 1)

    # Replace  H2
    text = re.sub('(\n//(?!/))(?P<id>.+)', '\n<h2>\g<id></h2>', text)

    # Replace  H3
    text = re.sub('(\n///(?!/))(?P<id>.+)', '\n<h3>\g<id></h3>', text)

    # Replace  H4
    text = re.sub('(\n////(?!/))(?P<id>.+)', '\n<h4>\g<id></h4>', text)

    # Replace IMG
    # img + link (external)
    text = re.sub(
        '(?P<prefix> |\n)img__http://(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__(?P<link>.*?)__',
        '\g<prefix><a href="\g<link>"><img src="http://\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" /></a>',
        text)
    # img + link (internal)
    text = re.sub(
        '(?P<prefix> |\n)img__(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__(?P<link>.*?)__',
        '\g<prefix><a href="\g<link>"><img src="static/images/\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" /></a>',
        text)
    # img only (external)
    text = re.sub(
        '(?P<prefix> |\n)img__http://(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__',
        '\g<prefix><img src="http://\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" />', text)
    # img only (internal)
    text = re.sub(
        '(?P<prefix> |\n)imgright__(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__',
        '\g<prefix><img src="static/images/\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" style="float:right" />',
        text)
    text = re.sub(
        '(?P<prefix> |\n)imgcenter__(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__',
        '\g<prefix><div class="row" style="text-align:center"><img src="static/images/\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" /></div>',
        text)
    text = re.sub('(?P<prefix> |\n)img__(?P<fileName>.*?)(?P<fileExt>\.gif|\.jpg|\.jpeg|\.png)__(?P<fileAlt>.*?)__',
                  '\g<prefix><img src="static/images/\g<fileName>\g<fileExt>" alt="\g<fileAlt>" title="\g<fileAlt>" />',
                  text)

    # Replace A
    # We add a space to all A near a special character or at the end of a line
    # We add a double space to A with already 1 space to preserve that space after linkFormat function
    text = re.sub('__(?P<link>(http://|/).*?)__ ', '__\g<link>__  ', text)
    text = re.sub('__(?P<link>(http://|/).*?)__(?P<anchor>\n|,|\.|;|\?|!|:|<)', '__\g<link>__ \g<anchor>', text)
    # All A followed by a space will be targeted
    text = re.sub('__(?P<id>(http://|/).*?)__ ', formatLink, text)

    # Replace  LI
    text = re.sub('(\n- (?P<id>.+))', '\n<li>\g<id></li>', text)

    # Replace TABLE
    text = re.sub('(!!)(?P<id>.*?)', '</td><td>', text)
    text = re.sub('\n\n</td><td>(?P<id>.*)',
                  '\n<table class="table table-bordered table-striped table-hover"><tr><td>\g<id>', text)
    text = re.sub('</td><td>\n</td><td>', '</td></tr>\n<tr><td>', text)
    text = re.sub('</td><td>\n\n', '</td></tr></table>\n\n', text)

    # Replace DOC
    text = re.sub('(?P<prefix> |\n)__(?P<fileName>.*?)__(?P<anchor>.*?)__',
                  '\g<prefix><a href="static/images/\g<fileName>">\g<anchor></a>', text)

    # Replace BR and P
    text = re.sub('\n(?!\n)(?!<h1|<h2|<h3|<li|<ul|<table|<tr|<td|</td)', '<br />', text)
    text = re.sub('\n<br />', '\n<p>', text)
    text = re.sub('\n<p>(?P<id>.*)', '\n<p>\g<id></p>', text)

    # Replace UL and LI
    text = re.sub('\n\n<li>(?P<id>.*)', '\n<ul><li>\g<id>', text)
    text = re.sub('</li>\n(?!<li>)', '</li></ul>\n', text)

    # Replace I
    text = re.sub('\*\*(?!\*)(?P<id>.*?)\*\*(?!\*)', '<i>\g<id></i>', text)

    # Replace B
    text = re.sub('\*(?!\*)(?P<id>.*?)\*(?!\*)', '<b>\g<id></b>', text)

    # Clean accidental empy tags
    text = re.sub('<p></p>', '', text)

    return text


def formatLink(match):
    g = match.groups()[0].partition('__')
    # No custom anchor
    if g[1] == '':
        return '<a href="' + g[0] + '">' + g[0] + '</a>'
    # Custom anchor found
    else:
        return '<a href="' + g[0] + '">' + g[2] + '</a>'
