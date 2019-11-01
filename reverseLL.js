class linkedListNode {
    constructor(data){
        this.data = data;
        this.next = null;
    }
    reverse(list){
        let traversal = list.next;
        let previous = list.data;
        let reverse = list;
        while(traversal != null){
            console.log(reverse,"linked next");
            reverse.next = previous;
            //console.log(reverse,"linked next");
            //console.log(previous,'previous');

            previous = traversal;
            //console.log(previous.data,"previous");

            //console.log(traversal.data);
           traversal = traversal.next; 
           //console.log("new loop\n");
        }
    }
}
const head = new linkedListNode(12);
head.next = new linkedListNode(37);
head.next.next = new linkedListNode(123);
head.next.next.next = new linkedListNode(49);

head.reverse(head);
