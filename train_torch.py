def run(model,train_data,valid_data,epochs = 0):

    model.train()
    optimizer1 = torch.optim.NAdam(model.parameters())

    total_y_losses,total_y_vlosses = [],[]
    
    for epoch in range(epochs):
        
        total_y_loss = 0
        total_y_vloss = 0
        
        for batch in train_data:
            x,y = batch
            
            x,y = x.to(DEVICE),y.to(DEVICE)
            
            x,y = x.float(),y.float()            
            
            optimizer1.zero_grad()
    
            y_pred = model(x)
            
            y_loss = F.mse_loss(y_pred.view(-1),y.view(-1))

            total_y_loss += y_loss.item()
    
            y_loss.backward()
    
            optimizer1.step()

        if epoch%3 == 0 : torch.save(model.state_dict(),f'saved_model{epoch}.pth')

        # total_y_losses.append(total_y_loss)

        with torch.no_grad():
            for i, vdata in enumerate(valid_data):
                x_v,y_v = vdata
                x_v,y_v = x_v.float(),y_v.float()
                vy_pred = model(x_v)
                yvloss = F.mse_loss(vy_pred.view(-1))
                total_y_vloss += yvloss
        # total_y_vlosses.append(total_y_vlosses)
            
    
        print(f'Epoch {epoch} Loss Y : {total_y_loss/len(train_data)} \n Valid Loss Y : {total_y_vloss/len(valid_data)}')
            