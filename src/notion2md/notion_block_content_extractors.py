from notional.blocks import Heading1

def heading_1_content_extractor(heading1:Heading1)->str:
    return ' '.join(text.text.content for text in heading1.heading_1.text)

def heading_2_content_extractor(heading2:Heading1)->str:
    return ' '.join(text.text.content for text in heading2.heading_2.text)

def heading_1_content_extractor(heading3:Heading1)->str:
    return ' '.join(text.text.content for text in heading3.heading_3.text)