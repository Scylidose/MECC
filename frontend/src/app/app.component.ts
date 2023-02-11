import {Component, ElementRef, ViewChild} from '@angular/core';
import {ChatbotApiService} from "./chatbot/chatbot-api.service";
import {Router} from "@angular/router";
import { DomSanitizer } from '@angular/platform-browser';

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

 constructor(private chatbotApi: ChatbotApiService, private router: Router, private _sanitizer: DomSanitizer) { }

 @ViewChild('chatListContainer') list?: ElementRef<HTMLDivElement>;

 chatInputMessage: string = "";
 human = {
    id: 1
  }

  bot = {
    id: 2
  }

  chatQuizResults: {
    quiz_result: Array<string>,
    score: any,
    topic_list: Array<string>
  } = {
    quiz_result: [],
    score: {},
    topic_list: []
  }

  chatYoutube: {
    message: string
  }[] = []

  chatUsefulLink: {
    link: string,
    title: string
  }[] = []

 chatMessages: {
  user: any,
  message: string,
  quick_replies: any,
  type: string
}[] = [
  {
    user: this.bot,
    message: "Hey!",
    quick_replies: [],
    type: "text"
  }
];

 ngOnInit() {

  var useful_link = [
    {
      link:"https://safety.google/security/security-tips/", title:"Google Safety Center"
    },
    {
      link:"https://staysafeonline.org/resources/", title:"Stay Safe Online"
    },
    {
      link:"https://www.securityroundtable.org/", title: "Cybersecurity Best Practices"
    },
    {
      link:"https://cyber.gc.ca/en", title:"Canadian Centre for Cyber Security"
    }
  ]

  this.chatUsefulLink = useful_link;

 }

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
  this.chatbot.messages = [{"df_type":"text", "text":quick_reply}];
  this.chatMessages.push({
    message:  quick_reply,
    quick_replies: [],
    user: this.human,
    type: "text"
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
  this.chatInputMessage = "";

  this.scrollToBottom();

  if(quick_reply == "Humans" || 
     quick_reply == "A weak encryption" ||
     quick_reply == "Short passwords"){
    this.chatbotApi.getResults().subscribe(data => {
      this.chatQuizResults = data
    });
  }

 };


receive(messages: Array<string>) {
  for(let i=0; i<messages.length; i++){
    messages[i] = messages[i].replace(/'/g, '"');
    var dict_message =JSON.parse(messages[i]);

    if(dict_message.text != ""){
      if(dict_message['df_type'] == 'text'){
        if(dict_message['text'].match(/youtube\.com/)) {
          const videoId = this.getId(dict_message['text']);
          var videoURL = '//www.youtube.com/embed/'+ videoId;
          dict_message['text'] = this._sanitizer.bypassSecurityTrustResourceUrl(videoURL);
          
          this.chatYoutube.push({
            message: dict_message['text']
          })
        } else {
          this.chatMessages.push({
            message: dict_message['text'],
            quick_replies: [],
            user: this.bot,
            type: dict_message['df_type']
          });
        }
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

getId(url: string) {
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|&v=)([^#&?]*).*/;
  const match = url.match(regExp);

  return (match && match[2].length === 11)
    ? match[2]
    : null;
}
 scrollToBottom() {
   const maxScroll = this.list?.nativeElement.scrollHeight;
   this.list?.nativeElement.scrollTo({top: maxScroll, behavior: 'smooth'});
 }
}