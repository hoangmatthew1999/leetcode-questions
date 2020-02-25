class linkedListNode {
    constructor(data){
        this.data = data;
        this.next = null;
    }
    reverse(list){
        let traversal = list.next;
        let previous = list.data;
        let reverse = null;
        
    }
}
const head = new linkedListNode(1);
head.next = new linkedListNode(2);
head.next.next = new linkedListNode(3);
head.next.next.next = new linkedListNode(4);

head.reverse(head);
