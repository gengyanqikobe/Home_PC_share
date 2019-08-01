


from pandas import DataFrame


from pandas import Series

import pandas

df = DataFrame()

df['a'] = [1,2,'3333']
df['b'] = [4,5,6]
print(df)


Header = """
    <html>
        <head>
            <meta charset="UTF-8">
        </head>
        <body>

        </body>
    </html>
    """

with open('df_to_html.html','w') as f:
    f.write(Header)
    f.write(df.to_html(classes='df'))
    f.close()