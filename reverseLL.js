class linkedListNode {
    constructor(data){
        this.data = data;
        this.next = null;
    }
    reverse(list){
        let previous = null;
        let current = list;
        let next;
        while(current != null){
            next = current.next;
            current.next = previous; //reversing 
            previous = current;
            current = next;
        }
        }
}
const head = new linkedListNode(1);
head.next = new linkedListNode(2);
head.next.next = new linkedListNode(3);
head.next.next.next = new linkedListNode(4);

head.reverse(head);
