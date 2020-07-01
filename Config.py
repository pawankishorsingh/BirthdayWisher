server = 'mailsea.sea.adobe.com'

sender = 'Pawan Kishor Singh<pksingh@adobe.com>'

cc = 'pawankishorsingh@gmail.com'

imageDirectory = "images"

html_header =   """\
			    <html>
			        <head>
			            <style>
				            body {font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;}
				            .body_text {color: orange; font-weight: bold;}
				            .header_footer_text {color: green; }				
				        </style>
			        </head>
			        <body>
			            <p class="header_footer_text">Dear %s</p>
			    """
html_body =     """
		            <p class="body_text">Wish you a very happy birthday today on %s.<br>Enjoy your special day to the fullest.</p>
		        """

html_footer =   """
                    <p class="header_footer_text">Regards<br>%s</p>
			        </body>
			    </html>
			    """

