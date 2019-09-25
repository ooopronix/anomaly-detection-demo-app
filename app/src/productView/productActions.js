import { CART, PRODUCTS, ROUTES } from "./productConstants"
import $ from "jquery";
import { setMessage } from "../message/messageActions";

export function addProduct (product) {
  return {
    type: CART.ADD,
    payload: product
  }
}

export function updateQuant (productId, quant) {
  return {
    type: PRODUCTS.UPDATE_QUANT,
    payload: {id:productId, quant:quant}
  }
}

export function removeProduct (productId) {
  return {
    type: CART.REMOVE,
    payload: productId
  }
}

export function clearProducts () {
  return {
    type: CART.CLEAR,
  }
}

export function setLoadingProducts(status){
  return {
    type: PRODUCTS.SET_LOADING_PRODUCTS,
    payload: status,
  }
}

export function setProducts(products){
  return {
    type: PRODUCTS.SET_PRODUCTS,
    payload: products,
  }
}

function parseResponse(result){
  let payload = {};
  result.products.map((product) => {
     payload[product.id] = product;
    }
  );
  return payload;
}

export function handleGETProducts(){
  const url = ROUTES.PRODUCTS;
  return (dispatch) => {
    dispatch(setLoadingProducts(true));
    // $.ajax({
    //   type: 'GET',
    //   url: url,
    //   dataType: 'json',
    //   success: function(result){
    //     let payload = parseResponse(result);
    //     dispatch(setProducts(payload));
    //     dispatch(setLoadingProducts(false));
    //   },
    //   error: function(){
    //     dispatch(setMessage('Could not successfully retrieve information from server', "danger"));
    //   },
    // });
    const payload = {"products": [{"id": "79161a98-30e0-11e7-b4e8-9801a798fc8f", "image": "bananas.jpg", "pname": "bananas", "pprice": 5.0, "pquant": 1, "ptype": "fruit"}, {"id": "7915f0cc-30e0-11e7-91c7-9801a798fc8f", "image": "onions.jpg", "pname": "onions", "pprice": 3.0, "pquant": 1, "ptype": "vegetables"}, {"id": "79169ffe-30e0-11e7-bf3b-9801a798fc8f", "image": "milk.jpg", "pname": "milk", "pprice": 4.0, "pquant": 1, "ptype": "dairy"}, {"id": "7916d9ba-30e0-11e7-b66f-9801a798fc8f", "image": "cheese.jpg", "pname": "cheese", "pprice": 3.0, "pquant": 3, "ptype": "dairy"}, {"id": "79165436-30e0-11e7-b79a-9801a798fc8f", "image": "almonds.jpg", "pname": "almonds", "pprice": 10.0, "pquant": 1, "ptype": "nuts"}]}
    dispatch(setProducts(parseResponse(payload)));
    dispatch(setLoadingProducts(false));
  };
}

export function selectProduct(product){
  return {
    type: PRODUCTS.SELECT_PRODUCT,
    payload: product,
  }
}

export function handleNewQuantChange(id, update){
  return {
    type: PRODUCTS.HANDLE_NEW_QUANT_CHANGE,
    payload: [id, update]
  }
}

