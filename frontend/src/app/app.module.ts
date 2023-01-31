import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {ChatbotApiService} from './chatbot/chatbot-api.service';

import {ChatbotFormComponent} from './chatbot/chatbot-form.component';
import {RouterModule, Routes} from '@angular/router';
import {ChatbotComponent} from './chatbot/chatbot.component';

const appRoutes: Routes = [
  { path: '', component: ChatbotFormComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    ChatbotFormComponent,
    ChatbotComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
    )
  ],
  providers: [ChatbotApiService],
  bootstrap: [AppComponent]
})
export class AppModule {
}