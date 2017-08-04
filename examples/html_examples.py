import examples.create_post as create_post

simple_html = '<html><head><style type="text/css">div.ena {color: red;} </style>' \
              '</head><body>bla <span style="color: #ff0000">bla</span> bla<<br/>' \
              '<div style="color: #ff0000">tri</div><br /><div class="ena">neki</div></body></html>'

bostjan_html = 'Normal text <br /><br /><a href="http://google.com" style="background-color: #4CAF50;' \
               'border: none; color: white; padding: 15px 32px; text-align: center; ' \
               'text-decoration: none; display: inline-block; font-size: 16px;">Go to Google</a>'

create_post.create_card_html_to_group_with_share_only_members('BTrdr5uoC1G52e51951b6c74c5082cb0523127b236b','lenko.smrkci@gmail.com', 'test1', bostjan_html)
a=2