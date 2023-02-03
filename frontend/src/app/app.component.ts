import {Component, ElementRef, ViewChild} from '@angular/core';
import {ChatbotApiService} from "./chatbot/chatbot-api.service";
import {Router} from "@angular/router";

@Component({
 selector: 'app-root',
 templateUrl: './app.component.html',
 styleUrls: ['./app.component.less']
})
export class AppComponent {
 title = 'chat-ui';

 message = "";

 chatbot = {
     messages: [""],
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
  message: string
}[] = [
  {
    user: this.bot,
    message: "Hello I'm MECC or Miscellaneous Educational Cybersecurity Chatbot\n"
  },
  {
    user: this.bot,
    message: "A chatbot specialized in cybersecurity education and sensibilization."
  }
];

 ngAfterViewChecked() {
   this.scrollToBottom()
 }


 saveChatbot() {
  this.chatbot.messages = [this.message];
  this.chatMessages.push({
    message:  this.message,
    user: this.human
  });
  this.chatbotApi.send(this.chatbot).subscribe(data => {
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

receive(messages: Array<string>) {
  for(let i=0; i<messages.length; i++){
    if(messages[i] != ""){
      this.chatMessages.push({
        message: messages[i],
        user: this.bot
      });
    }
  }
this.scrollToBottom()
}
 scrollToBottom() {
   const maxScroll = this.list?.nativeElement.scrollHeight;
   this.list?.nativeElement.scrollTo({top: maxScroll, behavior: 'smooth'});
 }
}