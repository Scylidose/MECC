import {AfterViewInit, Component, ElementRef} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {ChatbotApiService} from "./chatbot-api.service";
import {Router} from "@angular/router";

@Component({
  selector: 'chatbot-form',
  template: `
    <chatbot></chatbot>
    <div>
        <input id="chatbot-message" (keydown.enter)="saveChatbot()" (keyup)="updateMessage($event)">
    </div>
  `
})
export class ChatbotFormComponent {

    message = "";

    chatbot = {
        messages: "",
    };

  constructor(private chatbotApi: ChatbotApiService, private router: Router) { }

  updateMessage(event: any) {
    this.message = event.target.value;
  }

  saveChatbot() {
    this.chatbot.messages = this.message;
    this.chatbotApi
      .saveChatbot(this.chatbot)
      .subscribe(
        () => this.router.navigate(['/']),
        error => alert(error.message)
      );
   // window.location.reload();
  }
}

  