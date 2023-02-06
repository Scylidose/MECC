import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {FormsModule} from "@angular/forms";

import { ChatbotApiService } from './chatbot/chatbot-api.service';
import {HttpClient, HttpClientModule} from '@angular/common/http';


@NgModule({
 declarations: [
   AppComponent
 ],
 imports: [
   BrowserModule,
   HttpClientModule,
   AppRoutingModule,
   FormsModule
 ],
 providers: [ChatbotApiService],
 bootstrap: [AppComponent]
})
export class AppModule { }