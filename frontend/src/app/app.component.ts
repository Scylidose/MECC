import {Component, OnInit, OnDestroy} from '@angular/core';
import {Subscription} from 'rxjs';
import {ChatbotApiService} from './chatbot/chatbot-api.service';
import {Chatbot} from './chatbot/chatbot.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  chatbotListSubs: Subscription;
  chatbotList: Chatbot;

  constructor(private chatbotApi: ChatbotApiService) {
  }

  ngOnInit() {
    this.chatbotListSubs = this.chatbotApi
      .getChatbot()
      .subscribe(res => {
          this.chatbotList = res;
        },
        console.error
      );
  }

  ngOnDestroy() {
    this.chatbotListSubs.unsubscribe();
  }
}