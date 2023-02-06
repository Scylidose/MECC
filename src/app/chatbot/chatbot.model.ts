interface Dictionary<T> {
  [Key: string]: T;
}

export class Chatbot {
    constructor(
      public messages: Array<Dictionary<string>>
    ) { }
  }