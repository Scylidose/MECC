import {Component, ElementRef, ViewChild} from '@angular/core';
import {ChatbotApiService} from "./chatbot/chatbot-api.service";
import {Router} from "@angular/router";

interface Dictionary<T> {
  [Key: string]: T;
}

@Component({
 selector: 'app-root',
 templateUrl: './app.component.html',
 styleUrls: ['./app.component.less']
})
export class AppComponent {
 title = 'chat-ui';

 message = "";

 chatbot = {
     messages: [{"df_type":"", "text":""}],
 };

 constructor(private chatbotApi: ChatbotApiService, private router: Router) { }

 @ViewChild('chatListContainer') list?: ElementRef<HTMLDivElement>;
 chatInputMessage: string = "";
 human = {
    id: 1
  }

  bot = {
    id: 2
  }

 chatMessages: {
  user: any,
  message: string,
  quick_replies: any,
  type: string
}[] = [
  {
    user: this.bot,
    message: "Hello I'm MECC or Miscellaneous Educational Cybersecurity Chatbot\n",
    quick_replies: [],
    type: "text"
  },
  {
    user: this.bot,
    message: "A chatbot specialized in cybersecurity education and sensibilization.",
    quick_replies: [],
    type: "text"
  }
];

 ngAfterViewChecked() {
   this.scrollToBottom()
 }


 saveChatbot() {
  this.chatbot.messages = [{"df_type":"text", "text":this.message}];
  this.chatMessages.push({
    message:  this.message,
    quick_replies: [],
    user: this.human,
    type: "text"
  });
  this.chatbotApi.send(this.chatbot).subscribe(data => {
    console.log("-----------> ", data.messages);
    this.receive(data.messages);
  });
  this.chatbotApi
    .saveChatbot(this.chatbot)
    .subscribe(
      () => this.router.navigate(['/']),
      error => alert(error.message)
    );
  this.chatInputMessage = ""
  this.scrollToBottom()
}
replaceInput(quick_reply: string) { 
  console.log("REPLY : ", quick_reply);
  this.chatbot.messages = [{"df_type":"text", "text":quick_reply}];
  this.chatMessages.push({
    message:  quick_reply,
    quick_replies: [],
    user: this.human,
    type: "text"
  });
  this.chatbotApi.send(this.chatbot).subscribe(data => {
    console.log("-----------> ", data.messages);
    this.receive(data.messages);
  });
  this.chatbotApi
    .saveChatbot(this.chatbot)
    .subscribe(
      () => this.router.navigate(['/']),
      error => alert(error.message)
    );
  this.chatInputMessage = ""
  this.scrollToBottom()
 };

receive(messages: Array<string>) {
  for(let i=0; i<messages.length; i++){
    messages[i] = messages[i].replace(/'/g, '"');
    var dict_message =JSON.parse(messages[i]);
    if(dict_message.text != ""){
      console.log("---> ..", dict_message);
      if(dict_message['df_type'] == 'text'){
        this.chatMessages.push({
          message: dict_message['text'],
          quick_replies: [],
          user: this.bot,
          type: dict_message['df_type']
        });
      } else if(dict_message['df_type'] == 'quick_replies'){
        this.chatMessages.push({
          message: dict_message['text'],
          quick_replies: dict_message['quick_replies'],
          user: this.bot,
          type: dict_message['df_type']
        });
      }
    }
  }
this.scrollToBottom()
}
 scrollToBottom() {
   const maxScroll = this.list?.nativeElement.scrollHeight;
   this.list?.nativeElement.scrollTo({top: maxScroll, behavior: 'smooth'});
 }
}