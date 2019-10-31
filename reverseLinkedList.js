class linkedListNode {
    constructor(data){
        this.data = data;
        this.next = null;
    }
}
const head = new linkedListNode(12);
head.next = new linkedListNode(37);
console.log(head.next.data);