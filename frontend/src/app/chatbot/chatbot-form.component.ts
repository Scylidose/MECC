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
        <button id="send-message" (click)="saveChatbot()">Send Message</button>
    </div>
  `
})
export class ChatbotFormComponent {
  chatbot = {
    message: '',
    response: '',
  };

  constructor(private chatbotApi: ChatbotApiService, private router: Router) { }

  updateMessage(event: any) {
    this.chatbot.message = event.target.value;
  }

  updateResponse(event: any) {
    this.chatbot.response = event.target.value;
  }

  saveChatbot() {
    this.chatbotApi
      .saveChatbot(this.chatbot)
      .subscribe(
        () => this.router.navigate(['/']),
        error => alert(error.message)
      );
  }
}