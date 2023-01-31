import {Component} from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <div style="text-align:center">
      <h1>MECC</h1>
      <h4>Miscellaneous Educational Cybersecurity Chatbot</h4>
    </div>
    <router-outlet></router-outlet>
  `,
  styleUrls: ['./app.component.less']
})
export class AppComponent { }