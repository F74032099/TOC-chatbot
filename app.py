import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '396505069:AAEZCb1gBOxv1zKzOaxs0KOgBwoNbaQEh1o'
WEBHOOK_URL = 'https://2acfc9a1.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'description',
        'level1',
		'level2',
		'level3',
		'logic1',
		'logic2',
		'level1_err',
		'level3_correct',
		'logic1_reply',
		'logic2_reply'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'description',
            'conditions': 'is_going_to_description'
        },
		{	#back to init
			'trigger': 'advance',
            'source': ['level3','level2','level1'],
            'dest': 'user',
			'conditions': 'back_to_init'
		},
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'level1',
            'conditions': 'is_going_to_level1'
        },	
		{
			'trigger': 'advance',
            'source': 'level1',
            'dest': 'level2',
			'conditions': 'is_going_to_level2'
		},
		{
			'trigger': 'advance',
            'source': 'level2',
            'dest': 'level3',
			'conditions': 'is_going_to_level3'
		},
		{	
			'trigger': 'advance',
            'source': 'level3',
            'dest': 'level3_correct',
			'conditions': 'is_going_to_level3_correct'
		},
		
		{
			'trigger': 'advance',
            'source': 'user',
            'dest': 'logic1',
			'conditions': 'is_going_to_logic1'
		},
		{
			'trigger': 'advance',
            'source': 'logic1',
            'dest': 'logic2',
			'conditions': 'is_going_to_logic2'
		},
		{	#logic2 back to init
			'trigger': 'advance',
            'source': 'logic2',
            'dest': 'user',
			'conditions': 'logic_to_init'
		},
		{	#ans err
			'trigger': 'advance',
            'source': 'level3',
            'dest': 'level2',
			'conditions': 'wrong_ans'
		},
		{	#ans err
			'trigger': 'advance',
            'source': 'level2',
            'dest': 'level1',
			'conditions': 'wrong_ans'
		},
		{	#ans err
			'trigger': 'advance',
            'source': 'level1',
            'dest': 'level1_err',
			'conditions': 'wrong_ans'
		},
		
		{	
			'trigger': 'go_back',
            'source': 'level1_err',
            'dest': 'level1',
		},
		{	
			'trigger': 'go_back',
            'source': 'level3_correct',
            'dest': 'level3',
		},
		{	
			'trigger': 'go_back',
            'source': 'description',
            'dest': 'user',
		},
		{	
			'trigger': 'go_back',
            'source': 'logic1_reply',
            'dest': 'logic1',
		},
		{	
			'trigger': 'go_back',
            'source': 'logic2_reply',
            'dest': 'logic2',
		},
		{	#logic1 reply
			'trigger': 'advance',
            'source': 'logic1',
            'dest': 'logic1_reply',
			'conditions': 'user_response'
		},
		{	#logic2 reply
			'trigger': 'advance',
            'source': 'logic2',
            'dest': 'logic2_reply',
			'conditions': 'user_response'
		},
		
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
