from channels.consumer import SyncConsumer
from channels.exceptions import StopConsumer
from teaAdmin.models import QuizStatus

class myConsumer(SyncConsumer):

    def websocket_connect(self,event):
        print('Client is connected')

        self.send({
            'type' : 'websocket.accept',
        })
        
        
    
    def websocket_receive(self,event):
        print('client send somthing.. ',event['text'])

        self.status = event['text']

        if self.status == 'true':

            QuizStatus.objects.filter(isEnable = False).update(isEnable = True)

            self.send({
                'type' : 'websocket.send',
                'text' : '1' 
            })
        
        else:
            QuizStatus.objects.filter(isEnable = True).update(isEnable = False)
            self.send({
                'type' : 'websocket.send',
                'text' : '0' 
            })
        
    






    
    def websocket_disconnect(self,event):
        print('client  is diconneted..')
        self.send({'type' : 'websocket.close'})
        raise StopConsumer()
