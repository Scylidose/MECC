import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs';
import {ChatbotApiService} from './chatbot-api.service';
import {Chatbot} from './chatbot.model';

@Component({
  selector: 'chatbot',
  template: `
    <div>
        {{chatbot.message}}
    </div>
  `,
  styleUrls: ['../app.component.less']
})
export class ChatbotComponent implements OnInit, OnDestroy {
    chatbotSubs: Subscription;
    chatbot: Chatbot;
  
    constructor(private chatbotApi: ChatbotApiService) {
    }
  
    ngOnInit() {
      this.chatbotSubs = this.chatbotApi
        .getChatbot()
        .subscribe(res => {
            this.chatbot = res;
          },
          console.error
        );
    }
  
    ngOnDestroy() {
      this.chatbotSubs.unsubscribe();
    }
  }