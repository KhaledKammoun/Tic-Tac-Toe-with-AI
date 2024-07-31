export class User {
  constructor(public id: number, public name: string) {}

  public printUser() {
    return `User: ${this.id} : ${this.name}`;
  }
}
